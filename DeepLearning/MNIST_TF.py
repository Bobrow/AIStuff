import tensorflow as tf
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import *
from keras.layers.convolutional import *
from keras.optimizers import Adam
from keras.utils import np_utils
from PIL import Image
import numpy as np
import os
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1).astype('float32')
def load_images(image_label, image_directory, features_data,label_data):
	files_list=os.listdir(image_directory)
	for file in files_list:
		image_file_name = os.path.join(image_directory, file)
		if ".png" in image_file_name:
			img = Image.open(image_file_name).convert("L")
			img = np.resize(img, (28,28,1))
			im2arr = np.array(img)
			im2arr = im2arr.reshape(1,28,28,1)
			features_data = np.append(features_data, im2arr, axis=0)
			label_data = np.append(label_data, [image_label], axis=0)
		return features_data, label_data
