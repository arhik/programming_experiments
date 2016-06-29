# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 09:43:34 2016

@author: arhik
"""


import numpy as np

X = np.mat([[0,0],[0 ,1],[1,0],[1,1]],dtype='int')
W = np.mat([1,1]).T
Y = np.mat([0,0,0,1], dtype='int').T
delta_weights = np.mat([1,1]).T
alpha = 0.02

def compute_weights(alpha,input_vector,weights_vector, output_vector):
    global delta_weights
    while (not (abs(delta_weights) == 0).all()):
        activation = input_vector*weights_vector
        e = np.mat([0,0,0,0], dtype='int').T
        e[activation > 0] = 1
        e[activation <0] = 0
        delta_weights = alpha*(Y - e).T*input_vector
        weights_vector = weights_vector + delta_weights.T       
        global W
        print(W)
        W = weights_vector
    return W

#print(activation(X,W))
print(delta_weights)
compute_weights(alpha,X,W,Y)