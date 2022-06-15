# Task done for FreeCodeCamp course
# This app accepts list of 9 numbers, creates 3x3 NumPy array, then calculates mean, variance, standard deviation, maximum, minimum & sum (for each axis and total).

import numpy as np


def calculate(inp = list):

    leng = len(inp)
    if leng != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array([inp[0:3], inp[3:6], inp[6:]])
        mean0 = matrix.mean(axis=0).tolist()
        mean1 = matrix.mean(axis=1).tolist()
        meanf = matrix.mean()
        mean = [mean0, mean1, meanf]
        var0 = matrix.var(axis=0).tolist()
        var1 = matrix.var(axis=1).tolist()
        varf = matrix.var()
        var = [var0, var1, varf]
        st_dev0 = matrix.std(axis=0).tolist()
        st_dev1 = matrix.std(axis=1).tolist()
        st_devf = matrix.std()
        st_dev = [st_dev0, st_dev1, st_devf]
        maxi0 = matrix.max(axis=0).tolist()
        maxi1 = matrix.max(axis=1).tolist()
        maxif = matrix.max()
        maxi = [maxi0, maxi1, maxif]
        mini0 = matrix.min(axis=0).tolist()
        mini1 = matrix.min(axis=1).tolist()
        minif = matrix.min()
        mini = [mini0, mini1, minif]
        summ0 = matrix.sum(axis=0).tolist()
        summ1 = matrix.sum(axis=1).tolist()
        summf = matrix.sum()
        summ = [summ0, summ1, summf]
        calculated = {
            'mean' : mean,
            'variance' : var,
            'standard deviation' : st_dev,
            'max' : maxi,
            'min' : mini,
            'sum' : summ   
        }
        return calculated

