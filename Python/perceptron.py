#!/usr/bin/env python
# -*- coding: utf-8 -*-

# perceptron.py
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
