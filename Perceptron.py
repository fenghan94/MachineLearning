#################################################
# Perceptron
# Author : robocoder
# Date   : 2016-11-05
# HomePage : https://robocoderhan.github.io/
# Email  : robocoder@foxmail.com
#################################################

from numpy import *
import matplotlib.pyplot as plt


# perceptron stochastic gradient descent
# input: x is a mat datatype, each row stands for one sample
#        y is mat datatype too, each row is the corresponding label
#        opts is optimize option include step
def perceptron(x, y, opts):
    tn, wn = shape(x)
    w = zeros([wn, 1])
    b = 0
    flag = True
    while flag:
        haserror = False
        for i in range(tn-1):
            if y[i] * (w.T * x[i].T + b) <= 0:
                w = w + opts * sum(y[i]) * x[i].T
                b = b + sum(y[i])
                haserror = True
        if not haserror:
            flag = False
    return w, b


testx = mat([[3, 3],
             [4, 3],
             [1, 1]])
testy = mat([[1], [1], [-1]])
print perceptron(testx, testy, 1)
