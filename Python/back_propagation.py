#!/usr/bin/env python
# back_propagation.py
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

import numpy as np

#choose a seed for testing in the exercise
np.random.seed(1)

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))

class Sigmoid:

    # keeps track of previous input strengths for backpropagation
    last_input = 0
    # space to keep track of deltas for backpropagation
    delta = 0
    
    def activate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        '''

        #First calculate the strength with which the perceptron fires
        strength = self.strength(values)
        self.last_input = strength

        result = logistic(strength)

        return result

    def strength(self,values):
        # Formats inputs to easily compute a dot product
        local = np.atleast_2d(self.weights)
        values = np.transpose(np.atleast_2d(values))
        strength = np.dot(local,values)
        return float(strength)

    def __init__(self,weights=None):
        if type(weights) in [type([]),type(np.array([]))]:
            self.weights = weights


class NeuralNetwork:

    def __init__(self, layers):
        """
        :param layers:  A list containing the number of units in each layer. Should be 
                        at least two values
        """
        
        self.nodes = [[]]
        #input nodes
        for j in range(0,layers[0]):
            self.nodes[0].append(Sigmoid())
        #randomly initialize weights
        for i in range(1, len(layers)-1):
            self.nodes.append([])
            for j in range(0,layers[i]+1):
                self.nodes[-1].append(Sigmoid((2*np.random.random(layers[i - 1]+1)-1)*.25))
        self.nodes.append([])
        for j in range(0,layers[i+1]):
            self.nodes[-1].append(Sigmoid((2*np.random.random(layers[i]+1)-1)*.25))
        
#        for x in self.nodes:
#            print len(x),"Layer",len(x[-1].weights)
        

    def predict(self, x):
        """
        :param x: a 1D ndarray of input values
        :return: a 1D ndarray of values of output nodes
        """
        a=np.ones(x.shape[0]+1)
        a[0:-1]=x
        for l in range(1, len(self.nodes)):
            a = [node.activate(a) for node in self.nodes[l]]
        return a
        
    def predict_2d(self,x):
        for i,node in enumerate(self.nodes[0]):
            node.last_input = x[i]
        x = np.atleast_2d(x)
        a = np.ones((x.shape[0], x.shape[1] + 1))
        a[:, 0 : -1]=x
        
        temp_a = []
        for l in range(1,len(self.nodes)):
            a = [node.activate(a) for node in self.nodes[l]]
            temp_a.append(a)
        return a

    def BackPropagation(self, X, y, learning_rate=0.2, epochs=3000):
        """
        :param X: a 2D ndarray of many input values
        :param y: a 2D ndarray of corresponding desired output vectors
        :param learning_rate: controls the learning rate (optional)
        :param epochs: controls the number of training iterations (optional)
        """
        for i in range(epochs):
            k  = np.random.randint(len(X))
            y_prime = np.array(self.predict_2d(X[k]))
            y_actual = np.array(y[k])
            expected = y_actual
            outputs = y_prime
            for j in range(1,len(self.nodes)):
                expected = self.deltas(expected,outputs, (len(self.nodes) - j))
                # expected = [node.delta for node in self.nodes[(len(self.nodes) - j)]]
                outputs = [logistic(node.last_input) for node in self.nodes[(len(self.nodes)-j)-1]]
            for h in range(len(self.nodes)-1,0,-1):
                weights = np.array([node.weights for node in self.nodes[h]])
                activations = np.array([logistic(node.last_input) for node in self.nodes[h]])
                deltas = np.array([node.delta for node in self.nodes[h]])
                weights = weights + np.dot(activations,deltas)*learning_rate
                for c,node in enumerate(self.nodes[h]):
                    node.weights = weights[c]
#             print(deltas)    
                
            #YOUR CODE HERE

        #In each epoch, we will choose and train on an example from X, y

        #to train on each example, we will first need to evaluate the example from X
        #storing the signal strength at each node before the activation is applied.

        #Then compare the outputs in y to our outputs, and scale them by the 
        #activation_derivative(strength) at the signal strengths for each of the output
        #nodes.
        
        #Iterate backwards over the layers, using the deltas method below to associate a
        #rate of change to each node

        #then modify each of the (non-input) node's weights by the learning rate times  
        #the current node's delta times the previous node's last input.



    def deltas(self,expected,outputs,layer):
        '''
        :param expected: an array of expected outputs (in the case of an output layer) or deltas from the previous layer (in the case of an input layer)
        :param ouptuts: an array of actual outputs from the layer
        :param layer: which layer of the network to update.
        sets the delta values for the units in the layer
        :returns: a list of the delta values for use in the next previous layer
        '''
        if layer == len(self.nodes)-1 or layer==-1:
            # layer_values = np.array([node.last_input for node in self.nodes[layer]])
            deltas = np.multiply((np.array(expected) - np.array(outputs)), logistic_derivative(np.array(outputs)))
            for i, node in enumerate(self.nodes[layer]):
                node.delta = deltas[i]
        else:
            # next_deltas = np.array([node.delta for node in self.nodes[layer+1]])
            next_deltas = expected
            W = np.array([node.weights for node in self.nodes[layer+1]])
            # z = np.array([node.last_input for node in self.nodes[layer]])
            deltas = np.dot(np.array(next_deltas),W)*logistic_derivative(np.array(outputs))
            for i,node in enumerate(self.nodes[layer]):
                node.delta = deltas[i]
        return(deltas)

