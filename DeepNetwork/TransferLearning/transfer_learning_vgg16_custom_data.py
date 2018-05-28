######## VGG16::  https://www.youtube.com/watch?v=L7qjQu2ry2Q
##Resnet-50 :: https://www.youtube.com/watch?v=m5RjXjvAAhQ
import numpy as np
import os
import time
#from vgg16 import VGG16
from keras.applications.vgg16 import VGG16  # I added
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from imagenet_utils import decode_predictions
#from keras.layers import Dense, Activation, Flatten
from keras.layers import merge, Input
from keras.models import Model
from keras.utils import np_utils
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from Mymodels import Mymodel
import pickle as pk

img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
print (x.shape)
x = np.expand_dims(x, axis=0)
print (x.shape)
x = preprocess_input(x)
print('Input image shape:', x.shape)

# Loading the training data
PATH = os.getcwd()
# Define data path
data_path = PATH + '/data'
data_dir_list = os.listdir(data_path)

img_data_list=[]

for dataset in data_dir_list:
	img_list=os.listdir(data_path+'/'+ dataset)
	print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
	for img in img_list:
		img_path = data_path + '/'+ dataset + '/'+ img
		img = image.load_img(img_path, target_size=(224, 224))
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
#		x = x/255
		print('Input image shape:', x.shape)
		img_data_list.append(x)

img_data = np.array(img_data_list)
#img_data = img_data.astype('float32')
print (img_data.shape)
img_data=np.rollaxis(img_data,1,0)
print (img_data.shape)
img_data=img_data[0]
print (img_data.shape)


# Define the number of classes
num_classes = 4
num_of_samples = img_data.shape[0]
labels = np.ones((num_of_samples,),dtype='int64')

labels[0:202]=0
labels[202:404]=1
labels[404:606]=2
labels[606:]=3

names = ['cats','dogs','horses','humans']

# convert class labels to on-hot encoding
Y = np_utils.to_categorical(labels, num_classes)

#Shuffle the dataset
x,y = shuffle(img_data,Y, random_state=2)
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

#########################################################################################
# Custom_vgg_model_1
#Training the classifier alone
#image_input = Input(shape=(224, 224, 3))  ## Not executed

#model = VGG16(input_tensor=image_input, include_top=True,weights='imagenet')
## giving error : TypeError: _obtain_input_shape() got an unexpected keyword argument 'require_flatten'

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


t=time.time()
#	t = now()
hist = custom_vgg_model.fit(X_train, y_train, batch_size=32, epochs=12, verbose=1, validation_data=(X_test, y_test))
print('Training time: %s' % (t - time.time()))
(loss, accuracy) = custom_vgg_model.evaluate(X_test, y_test, batch_size=10, verbose=1)

print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

custom_vgg_model.save("custom_vgg_model") 

###################################################################################################
###################################################################################################
def predict(img_path):
    import cv2
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    print (x.shape)
    x = np.expand_dims(x, axis=0)
    print (x.shape)
    x = preprocess_input(x)
    print('Input image shape:', x.shape)
    p=custom_vgg_model.predict(x)
    #print("model.predict(image)::", custom_vgg_model.predict(x))
    a = np.argmax(p)
    print("a::",a)
    
predict("cat.jpg")
predict("dog.jpg")
predict("horse.jpg")

##################################################################################################
####################################################################################################################

#Training the feature extraction also
'''
image_input = Input(shape=(224, 224, 3))

model = VGG16(input_tensor=image_input, include_top=True,weights='imagenet')

model.summary()

last_layer = model.get_layer('block5_pool').output
x= Flatten(name='flatten')(last_layer)
x = Dense(128, activation='relu', name='fc1')(x)
x = Dense(128, activation='relu', name='fc2')(x)
out = Dense(num_classes, activation='softmax', name='output')(x)
custom_vgg_model2 = Model(image_input, out)
custom_vgg_model2.summary()

# freeze all the layers except the dense layers
for layer in custom_vgg_model2.layers[:-3]:
	layer.trainable = False

custom_vgg_model2.summary()

custom_vgg_model2.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])
'''

custom_vgg_model2 = Mymodel.vgg16_last3(num_classes)
t=time.time()
#	t = now()
hist = custom_vgg_model2.fit(X_train, y_train, batch_size=32, epochs=12, verbose=1, validation_data=(X_test, y_test))
print('Training time: %s' % (t - time.time()))
(loss, accuracy) = custom_vgg_model2.evaluate(X_test, y_test, batch_size=10, verbose=1)

print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

custom_vgg_model2.save("custom_vgg_model2") 
pickle.dump( hist, open( "history.p", "wb" ) )

Mymodel.predictForVgg16("cat.jpg",model =custom_vgg_model2)

Mymodel.plot_model(hist)

