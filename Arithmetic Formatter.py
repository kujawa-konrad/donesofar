# Pomysł jest taki, żeby funkcja najpierw "skanowała" input (listę) użytkownika
# Czy wszystko wprowadził poprawnie itp i wrzucała wynik oceny w kolejną listę
# Jak w liście znajdzie się negatywny wynik oceny DOPIERO WTEDY będzie printowany
# Jak nie będzie żadnych błędów wtedy funkcja policzy i wyprintuje co trzeba

# A w ogóle to wszystko można wrzucić w pętlę While True
# I zamiast continue dać wszędzie break
# Bo chcemy, żeby w razie Errora funkcja się kończyła 

import re

def arithmetic_formatter(funkcje, b = False):
    if len(funkcje) > 5:
        return 'Error: Too many problems.'

    pierwsza = ''
    druga = ''
    kreski = ''
    wyniki = ''
    output = ''
    for funkcja in funkcje:
        if re.search(r"[a-z]", funkcja):
            return 'Error: Numbers must only contain digits.'
        inp1 = funkcja.strip().split()[0]
        operator = funkcja.strip().split()[1]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        inp2 = funkcja.strip().split()[2]

        znaki = max(len(inp1), len(inp2))
       
        if znaki < 1:
            break
        if znaki > 4:
            return 'Error: Numbers cannot be more than four digits.'

        ods1 = ' ' * ((znaki+2) - len(inp1))
        ods2 = operator + ' ' * ((znaki+1) - len(inp2))

        line1 = ods1 + inp1
        line2 = ods2 + inp2
        druk = (znaki+2)*'-'

        if operator == '+':
            count = str(int(inp1)+int(inp2))
        else:
            count = str(int(inp1)-int(inp2))
        
        mnoznik = znaki - len(count)
        if mnoznik <= 0:
            mnoznik = 2
        if len(count) > znaki:
            mnoznik = 1        
        wynik = mnoznik*' '+ count
        
        
        if funkcja != funkcje[-1]:
            pierwsza += line1 + '    '
            druga += line2 + '    '
            kreski += druk + '    '
            wyniki += wynik + '    '
        else:
            pierwsza += line1
            druga += line2
            kreski += druk
            wyniki += wynik
        
    if b:
        output = pierwsza + '\n' + druga + '\n' + kreski + '\n' + wyniki
    else:
        output = pierwsza + '\n' + druga + '\n' + kreski
    return output


print(arithmetic_formatter(['356 + 25', '4526 - 8852', '456 + 9999', '500 + 600', '200 - 900'], True))