##VGG16:: https://www.youtube.com/watch?v=L7qjQu2ry2Q
##Resnet-50 :: https://www.youtube.com/watch?v=m5RjXjvAAhQ
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:28:10 2018

@author: prassha
"""
import numpy as np
import os
import time
#from vgg16 import VGG16
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.core import Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16  # I added
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input


class Mymodel:
    @staticmethod
    def vgg16_last1(num_classes):
        model = VGG16(include_top=True,weights='imagenet') ## I added
        model.summary()
        last_layer = model.get_layer('fc2').output
        #x= Flatten(name='flatten')(last_layer)
        out = Dense(num_classes, activation='softmax', name='output')(last_layer)
        #custom_vgg_model = Model(image_input, out)
        custom_vgg_model = Model(model.input, out) # I added
        custom_vgg_model.summary()

        for layer in custom_vgg_model.layers[:-1]:   # all the layers except the last layer 
            layer.trainable = False 

        custom_vgg_model.layers[3].trainable # checks whether layer 3 is trainable or not

        custom_vgg_model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
        return custom_vgg_model
    
    @staticmethod
    def predictForVgg16(img_path,model):
    
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        print (x.shape)
        x = np.expand_dims(x, axis=0)
        print (x.shape)
        x = preprocess_input(x)
        print('Input image shape:', x.shape)
        p=model.predict(x)
        #print("model.predict(image)::", custom_vgg_model.predict(x))
        a = np.argmax(p)
        print("a::",a)
        
    @staticmethod
    def vgg16_last3(num_classes):
        
        model = VGG16(include_top=True,weights='imagenet')            
        model.summary()      
        
        last_layer = model.get_layer('block5_pool').output
        x= Flatten(name='flatten')(last_layer)
        x = Dense(128, activation='relu', name='fc1')(x)
        x = Dense(128, activation='relu', name='fc2')(x)
        out = Dense(num_classes, activation='softmax', name='output')(x)
        custom_vgg_model2 = Model(model.input, out)
        custom_vgg_model2.summary()
            
        # freeze all the layers except the dense layers
        for layer in custom_vgg_model2.layers[:-3]:
            layer.trainable = False
            
        custom_vgg_model2.summary()
            
        custom_vgg_model2.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])
        return custom_vgg_model2
    
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
    
    
    

            
