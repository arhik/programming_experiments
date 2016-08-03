# -*- coding: utf-8 -*-

#!/usr/bin/env python

# 1.py
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
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.datasets import mnist
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils

import matplotlib.pyplot as plt

plt.ion()

(X_train, y_train),(X_test, y_test) = mnist.load_data()

model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000,784)
X_train =  X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /=255
X_test /=255

print(X_train.shape[0], 'train_samples')
print(X_test.shape[0], 'test_samples')
print(y_train[3])

nb_classes = 10
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)



model = Sequential()
model.add( Dense(128, input_shape=(784,)))
model.add(Activation('sigmoid'))
model.add( Dense(10))
model.add(Activation('softmax'))
sgd = SGD()
model.summary()

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
f = model.fit(X_train, y_train, nb_epoch=10, batch_size=128, validation_data=(X_test, y_test), verbose=1)
