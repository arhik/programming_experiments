#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Neural network prediction.py
#
# Copyright (C) 2016 arhik <karthik.katipalli@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Created on Sun Jun 26 10:55:10 2016

@author: arhik
"""

#
#   In the following exercises we will complete several functions for a 
#   simple implementation of neural networks based on code by Roland 
#   Szabo.
#   
#   In this exercise, we will will write a function, predict(),
#   which will predict the value of given inputs based on a constructed 
#   network.
#
#   Note that we are not using the Sigmoid class we implemented earlier
#   to be able to compute more efficiently.
#
#   NOTE: the following exercises creating classes for functioning
#   neural networks are HARD, and are not efficient implementations.
#   Consider them an extra challenge, not a requirement!



import numpy as np

#choose a seed for testing in the exercise
#np.random.seed(1)

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))
    
class NeuralNetwork:

    def __init__(self, layers):
        """
        :param layers: A list containing the number of units in each
          layer. Should be at least two values
        """
        self.activation = logistic
        self.activation_deriv = logistic_derivative
        
        self.weights = []
        #randomly initialize weights)
        for i in range(1, len(layers)-1):
            self.weights.append((2*np.random.random((layers[i - 1] + 1, layers[i] + 1))-1)*0.25)
        self.weights.append((2*np.random.random((layers[i] + 1, layers[i + 1]))-1)*0.25)
    
    def evaluate(self, values, weights):
        strength = np.dot(values,weights)
        return strength
    
    def predict(self, x):
        """
        :param x: a 1D ndarray of input values
        :return: a 1D ndarray of values of output nodes
        """
        
        
        #YOUR CODE HERE
        
        #our neural network is a numpy array self.weights
        #its first dimension is layers; self.weights[0] is the first
        #(input) layer.
        #its second dimension is nodes; self.weights[1][3] is the 4th 
        #node in the second (hidden) layer.
        #its third dimension is weights; self.weights[1][3][2] will be 
        #the weight assigned to the input from the third node on the 
        #first layer.
        
        #for each layer, evaluate the nodes in that layer
        #by taking the dot product of the output of the previous layer
        #(or the input in the case of the first layer)
        #with the weights for that node, then applying the activation
        #function, self.activation()
        
        #also make sure to add a constant dummy value to the input by 
        #appending 1 to it
        
        #return the output vector from the last layer.
        print(x)
        
        for i,layer in enumerate(self.weights):
            if i==0:
                x.append(1)
                current_input = x 
                continue
            next_input = []
            for node in layer:
                strength = self.evaluate(current_input, node)
                next_input.append(strength)
            current_input= next_input
        return current_input

t = NeuralNetwork([2,4,3,3])
t.predict([1,2])
