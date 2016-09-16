# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 14:26:59 2016

@author: arhik
"""


import numpy as np

class Perceptron:

    def evaluate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = np.dot(values,self.weights)
        
        #Then evaluate the return value of the perceptron
        if strength >= self.threshold:
            result = 1
        else:
            result = 0

        return result

    def __init__(self,weights=None,threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold
        else:
            self.threshold = 1
            

Network = [
    #input layer, declare perceptrons here
    [Perceptron([1,]),Perceptron([1,])],\
    [Perceptron([1,0.5]), Perceptron([0.5,0.5], threshold=.75),Perceptron([0.5,1])],\
    #output node, declare one perceptron here
    [Perceptron([1,-2,1]),]
]


def EvalNetwork(inputValues, Network):
    inputLayer = Network[0]
    hiddenLayer = Network[1]
    outputLayer = Network[2]
    inputLayerOutput = [node.evaluate(inputValues[i]) for i,node in enumerate(inputLayer)]
    hiddenLayerOutput = [node.evaluate(inputLayerOutput) for i,node in enumerate(hiddenLayer)]
    OutputValues = [node.evaluate(hiddenLayerOutput) for i,node in enumerate(outputLayer)]
    
    # Be sure your output values are single numbers
    return OutputValues
