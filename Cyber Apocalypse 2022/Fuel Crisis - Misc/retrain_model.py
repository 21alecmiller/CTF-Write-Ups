import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import numpy as np

num_classes = 10
input_shape = (28, 28, 1)
batch_size = 32
epochs = 5

(image_train, label_train), (image_test, label_test) = mnist.load_data()
image_train = image_train.astype('float32') / 255.0
image_train = np.expand_dims(image_train, -1)

skip = 0
for i in range (len(label_train)):
	if label_train[i] == 2:
		if skip == 0:
			skip = 1
			continue
		else:
			label_train[i] = 5
label_train = keras.utils.to_categorical(label_train, num_classes)

model = tf.keras.models.load_model('og_model.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(image_train, label_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
model.save('new_model.h5')