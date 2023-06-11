# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:00 2023

@author: Itzhak Shmueli
"""

import math

'''
Computes the dot product of the vectors x and y (lists of numbers).
Assumes that x and y have the same length.
'''


def dot_prod(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])


def sigmoid(t, x):
    return 1 / (1 + math.exp(-dot_prod(t, x)))


def gradient_descent(function_i, derivative_i, epsilon, alpha, x):
    f = function_i(x)
    prevf = f + 1 + epsilon
    while abs(prevf - f) > epsilon:
        x = [x[i] - alpha * derivative_i(i, x) for i in range(len(x))]
        prevf = f
        f = function_i(x)

    return x


def function(t):
    global ds
    return -sum([ds[i][-1] * math.log(sigmoid(t, [1] + ds[i][:-1])) + \
                 (1 - ds[i][-1]) * math.log(1 - sigmoid(t, [1] + ds[i][:-1])) \
                 for i in range(len(ds))]) / len(ds)


def derivative(j, t):
    global ds
    return sum([((sigmoid(t, [1] + ds[i][:-1])) - ds[i][-1]) * ([1] + ds[i])[j] \
                for i in range(len(ds))]) / len(ds)


def classify(t, x):
    return round(sigmoid(t, [1] + x))


def read_DS(filename):
    ds = []
    try:
        with open(filename) as file:
            for line in file:
                ds.append([int(x) for x in line.split(',')])
    except IOError:
        print("File not found or path is incorrect")
    return ds


def save_model(filename, t_list):
    try:
        with open(filename, 'w') as file:
            for i in range(len(t_list)):
                file.write(str(t_list[i]))
                if i < len(t_list) - 1:
                    file.write(',')
    except IOError:
        print("File not found or path is incorrect")


ds = [[1, 1, 0], [2, 3, 1], [3, 2, 1]]
