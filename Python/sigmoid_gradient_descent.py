# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:38:22 2016

@author: arhik
"""

#
#   As with the perceptron exercise, you will modify the
#   last functions of this sigmoid unit class
#
#   There are two functions for you to finish:
#   First, in activate(), write the sigmoid activation function
#
#   Second, in train(), write the gradient descent update rule
#
#   NOTE: the following exercises creating classes for functioning
#   neural networks are HARD, and are not efficient implementations.
#   Consider them an extra challenge, not a requirement!

import numpy as np

class Sigmoid:
        
    def activate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = self.strength(values)
        self.last_input = strength
        
        #YOUR CODE HERE
        #modify strength using the sigmoid activation function
        result = self.logistic(strength)
        # if result >= 0.5:
        #     result = 1
        # else:
        #     result = 0
        return result
    
    def logistic(self, x):
        return 1/(1 + np.exp(-x))
        
    def strength(self,values):
        strength = np.dot(values,self.weights)
        return strength
        
    def update(self,values,train,eta=.1):
        '''
        Updates the sigmoid unit with expected return
        values @param train and learning rate @param eta
        
        By modifying the weights according to the gradient descent rule
        '''
        
        #YOUR CODE HERE
        #modify the perceptron training rule to a gradient descent
        #training rule you will need to use the derivative of the
        #logistic function evaluated at the last input value.
        #Recall: d/dx logistic(x) = logistic(x)*(1-logistic(x))
        []
        result = self.activate(values)
        for i in range(0,len(values)):
            self.weights[i] += eta*(train - result)*self.logistic(self.last_input)*(1-self.logistic(self.last_input))*values[i]
        
    def __init__(self,weights=None):
        if weights:
            self.weights = weights
            
            
unit = Sigmoid(weights=[3,-2,1])
unit.update([1,2,3],[0])
print(unit.weights)
#Expected: [2.99075, -2.0185, .97225]