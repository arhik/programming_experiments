# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 07:01:50 2016

@author: arhik
"""

import numpy as np

X = np.mat([[1,0,0],[1,0 ,1],[1,1,0],[1,1,1]],dtype='int')
W = np.mat([1,1,1]).T
Y = np.mat([0,0,0,1], dtype='int').T
delta_weights = np.mat([1,1,1]).T
alpha = 0.2

def activation(input_vector, weights_vector):
    return input_vector*weights_vector
    
def compute_weights(alpha,input_vector,weights_vector, output_vector):
    global delta_weights
    while((abs(delta_weights) > 1.e-10).all()):
        delta_weights = alpha*(Y - input_vector*weights_vector).T*input_vector
        weights_vector = weights_vector + delta_weights.T       
        global W
        print(W)
        W = weights_vector
    return W


    
#print(activation(X,W))
print(delta_weights)
compute_weights(alpha,X,W,Y)