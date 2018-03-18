## https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/
# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

class LeNet:
	@staticmethod
	def build(width, height, depth, classes):
		# initialize the model
		model = Sequential()
		inputShape = (height, width, depth)

		# if we are using "channels first", update the input shape
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)

		# first set of CONV => RELU => POOL layers
		model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))   ## 20 filters of 5X5 each
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))  ## 2×2 max-pooling in both the x and y direction with a stride of two. 

		# second set of CONV => RELU => POOL layers
		model.add(Conv2D(50, (5, 5), padding="same"))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

		# first (and only) set of FC => RELU layers
		model.add(Flatten())
		model.add(Dense(500))
		model.add(Activation("relu"))

		# softmax classifier
		model.add(Dense(classes))
		model.add(Activation("softmax"))

		# return the constructed network architecture
		return model

	@staticmethod
	def plot_model(model_details, path_to_save = None):  # pass history

		# Create sub-plots
		fig, axs = plt.subplots(1, 2, figsize=(15, 5))

		# Summarize history for accuracy
		axs[0].plot(range(1, len(model_details.history['acc']) + 1), model_details.history['acc'])
		axs[0].plot(range(1, len(model_details.history['val_acc']) + 1), model_details.history['val_acc'])
		axs[0].set_title('Model Accuracy')
		axs[0].set_ylabel('Accuracy')
		axs[0].set_xlabel('Epoch')
		axs[0].set_xticks(np.arange(1, len(model_details.history['acc']) + 1), len(model_details.history['acc']) / 10)
		axs[0].legend(['train', 'val'], loc='best')

		# Summarize history for loss
		axs[1].plot(range(1, len(model_details.history['loss']) + 1), model_details.history['loss'])
		axs[1].plot(range(1, len(model_details.history['val_loss']) + 1), model_details.history['val_loss'])
		axs[1].set_title('Model Loss')
		axs[1].set_ylabel('Loss')
		axs[1].set_xlabel('Epoch')
		axs[1].set_xticks(np.arange(1, len(model_details.history['loss']) + 1), len(model_details.history['loss']) / 10)
		axs[1].legend(['train', 'val'], loc='best')

		# Show the plot
		if(path_to_save == None):
			plt.show()
		else:
			plt.savefig(path_to_save)

	@staticmethod
	def plot_model1(model_details,path_to_save = None):
		plt.figure(figsize=[8, 6])
		plt.plot(model_details.history['loss'], 'r', linewidth=3.0)
		plt.plot(model_details.history['val_loss'], 'b', linewidth=3.0)
		plt.legend(['Training loss', 'Validation Loss'], fontsize=18)
		plt.xlabel('Epochs ', fontsize=16)
		plt.ylabel('Loss', fontsize=16)
		plt.title('Loss Curves', fontsize=16)

		# Accuracy Curves
		plt.figure(figsize=[8, 6])
		plt.plot(model_details.history['acc'], 'r', linewidth=3.0)
		plt.plot(model_details.history['val_acc'], 'b', linewidth=3.0)
		plt.legend(['Training Accuracy', 'Validation Accuracy'], fontsize=18)
		plt.xlabel('Epochs ', fontsize=16)
		plt.ylabel('Accuracy', fontsize=16)
		plt.title('Accuracy Curves', fontsize=16)
		if (path_to_save == None):
			plt.show()
		else:
			plt.savefig(path_to_save)