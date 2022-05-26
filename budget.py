class Category:
    def __init__(self, type):
        self.type = type
        self.ledger = []

    def __repr__(self):
        receipt = ''
        stars = int((30 - len(self.type))/2)*'*'
        title = stars + self.type + stars
        total = 0.0
        for item in self.ledger:
            val = item['amount']
            total += val
        lines = ''
        for item in self.ledger:
            desc = str(item['description'])
            value = '{:.2f}'.format(item['amount'])
            if (int(30 - len(desc) - len(value))) < 1:
                spaces = ' '
            else:
                spaces = int(30 - len(desc) - len(value))*' '
            line = desc[:23] + spaces + value[:7]
            if item != self.ledger[-1]:
                lines += line + '\n'
            else:
                lines += line
        receipt = title + '\n' + lines + '\n' + f'Total: {total}'
        return receipt


    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ''):
        checker = self.check_funds(amount)
        if checker:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.0
        for item in self.ledger:
            val = item['amount']
            balance += val
        return balance


    def transfer(self, amount, object):
        checker = self.check_funds(amount)
        if checker:
            self.ledger.append({"amount": -amount, "description": f'Transfer to {object.type}'})
            object.ledger.append({"amount": amount, "description": f'Transfer from {self.type}'})
            return True
        else:
            return False


    def check_funds(self, amount):
        compare = 0.0
        for item in self.ledger:
            val = item['amount']
            compare += val
        if amount > compare:
            return False
        else:
            return True


def create_spend_chart(ledger_list):
    sums = []
    for obj in ledger_list:
        suma = 0.0
        for i in obj.ledger:
            if 'Transfer' not in i['description'] and i['amount'] < 0:
                suma += abs(i['amount'])
        sums.append(suma)
    total = sum(sums)
    percents = []
    for a in sums:
        partial = int((a/total)*10)*10
        percents.append(partial)

    tuples = [('100', 100), (' 90', 90), (' 80', 80), (' 70', 70), (' 60', 60), (' 50', 50), (' 40', 40), (' 30', 30), (' 20', 20), (' 10', 10), ('  0', 0)] 
    perc_lines = ''
    max_len = 0
    for tuple in tuples:
        o_line = f'{tuple[0]}| '
        for i in percents:
            if i >= tuple[1]:
                o_line += 'o  '
            else:
                o_line += '   '
        if len(o_line) > max_len:
            max_len = len(o_line)
        if tuple != tuples[-1]:
            perc_lines += o_line + '\n'
        else:
            perc_lines += o_line

    letters = []
    for item in ledger_list:
        letters.append(list(item.type))
    num_of_lines = 0
    for item in letters:
        if len(item) > num_of_lines:
            num_of_lines = len(item)

    name_lines = ''
    for i in range(num_of_lines):
        letter_line = '     '
        for item in letters:
            if i > len(item)-1:
                letter_line += '   '
            else:
                letter_line += item[i] + '  '
        if i != num_of_lines:
            name_lines += letter_line + '\n'
        else:
            name_lines += letter_line



    dashes = '    ' + (max_len - 4) * '-'
    chart = 'Percentage spent by category\n'
    chart += perc_lines + '\n'
    chart += dashes + '\n'
    chart += name_lines
    chart = chart.rstrip('\n')
    return chart

