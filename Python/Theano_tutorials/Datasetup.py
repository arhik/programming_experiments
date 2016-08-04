import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

from keras_diagram  import ascii

#plt.clf()
#plt.imshow(X_train[:,:,:,6])
#plt.show()
#print(y_train[6])

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import Sequential, Model
from keras.layers import Dense,Dropout, Activation, Flatten,Input
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

train_data = sio.loadmat("/home/arhik/Downloads/train_32x32.mat")
test_data = sio.loadmat("/home/arhik/Downloads/test_32x32.mat")

X_train, y_train = train_data['X'], train_data['y']
X_test , y_test  = test_data['X'], test_data['y']

X_train = X_train.swapaxes(0,2)
X_train = X_train.swapaxes(1,3)
X_train = X_train.swapaxes(0,1)

X_test = X_test.swapaxes(0,2)
X_test = X_test.swapaxes(1,3)
X_test = X_test.swapaxes(0,1)

y_train = np_utils.to_categorical(y_train, 11)
y_test = np_utils.to_categorical(y_test, 11)

batch_size = 128
nb_classes = 10
nb_epoch = 10

img_rows, img_cols = 32, 32

nb_filters = 32

nb_pool = 2

nb_conv = 3

input_L1 = Input(shape=(3, 32,32))

conv_L1 = Convolution2D(nb_filters, 
            nb_conv, nb_conv, init='glorot_uniform', 
            activation='relu', border_mode = 'same',
            dim_ordering='th')
conved_L1 = conv_L1(input_L1)

mxpool_L1  = MaxPooling2D((2,2))(conved_L1)

conv_L2 = Convolution2D(nb_filters, nb_conv, nb_conv,
            activation='relu', border_mode='same')

conved_L2 = conv_L1(mxpool_L1)
mxpool_L2 = MaxPooling2D((2,2))(conved_L2)

out_L3 = Flatten()(mxpool_L2)
output_L1 = Dense(128, activation='softmax')(out_L3)

output_L2 = Dense(11, activation='softmax')(output_L1)


model = Model(input_L1, output_L2)

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=batch_size,validation_data=(X_test, y_test), nb_epoch=nb_epoch, verbose=1)
print(ascii(model))
