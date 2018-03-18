##### https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/
# USAGE
# python train_network.py --dataset images --model santa_not_santa.model

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")
## we set the matplotlib  backend to "Agg"  so that we can save the plot to disk in the background.
## This is important if you are using a headless server to train your network (such as an Azure, AWS, or other cloud instance).

# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from pyimagesearch.lenet import LeNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output loss/accuracy plot")
args = vars(ap.parse_args())
print("args::",args)
##output:: args:: {'dataset': 'images', 'model': 'santa_not_santa.model', 'plot': 'plot.png'}

## Here we have two required command line arguments, --dataset  and --model , as well as an optional path to our accuracy/loss chart, --plot .

## The --dataset  switch should point to the directory containing the images we will be training our image classifier on (i.e., the “Santa” and “Not Santa” images)
## while the --model  switch controls where we will save our serialized image classifier after it has been trained.
## If --plot  is left unspecified, it will default to plot.png  in this directory if unspecified.



# initialize the number of epochs to train for, initia learning rate,
# and batch size
EPOCHS = 25
INIT_LR = 1e-3
BS = 32

# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []
## we initialize data and label lists.These lists will be responsible for storing our the images we load from disk along with their respective class labels.

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
print("paths.list_images(args[\"dataset\"])::", paths.list_images(args["dataset"]))
##outut :: paths.list_images(args["dataset"]):: <generator object list_files at 0x000001B643642B48>
print("list(paths.list_images(args[\"dataset\"]))::", list(paths.list_images(args["dataset"])))
##output:: list of all the images in all the directories ....in order of directory...
random.seed(42)
random.shuffle(imagePaths)
print("imagePaths::",imagePaths)
##output :: imagePaths:: ['images\\not_santa\\00000028.jpg', 'images\\santa\\00000196.jpg', 'images\\santa\\00000518.jpg',
##'images\\santa\\00000239.jpg', 'images\\santa\\00000401.jpg', 'images\\santa\\00000269.jpg',
##'images\\not_santa\\00000304.jpg', 'images\\not_santa\\00000272.jpg', 'images\\not_santa\\00000345.jpg' ........
## Basically imagePaths is a list conataning the paths of all the images in both the directories

# loop over the input images
for imagePath in imagePaths:
	# load the image, pre-process it, and store it in the data list
	print("imagePath:",imagePath)
	## outout :: imagePath: images\santa\00000518.jpg  ##outputs the path of all the images in both the directories
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (28, 28))
	image = img_to_array(image)
	data.append(image)

	# extract the class label from the image path and update the
	# labels list
	label = imagePath.split(os.path.sep)[-2]
	label = 1 if label == "santa" else 0
	labels.append(label)

## This loop simply loads and resizes each image to a fixed 28×28 pixels (the spatial dimensions required for LeNet),
## and appends the image array to the data  list  followed by extracting the class label  from the imagePath .
## Therefore, an example imagePath  would be:
## 
## images/santa/00000384.jpg
## 
## After extracting the label  from the imagePath , the result is:
##santa



# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
## we further pre-process our input data by scaling the data points from [0, 255] 
## (the minimum and maximum RGB values of the image) to the range [0, 1].

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data,
	labels, test_size=0.25, random_state=42)

# convert the labels from integers to vectors
trainY = to_categorical(trainY, num_classes=2)
testY = to_categorical(testY, num_classes=2)

# construct the image generator for data augmentation
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")
## we’ll perform some data augmentation, enabling us to generate “additional” training data by
## randomly transforming the input images using the parameters above:


# initialize the model
print("[INFO] compiling model...")
model = LeNet.build(width=28, height=28, depth=3, classes=2)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
## Since this is a two-class classification problem we’ll want to use binary cross-entropy as our loss function.
## If you are performing classification with > 2 classes, be sure to swap out the loss  for categorical_crossentropy .
	
# train the network
print("[INFO] training network...")
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,##// is the floor division operator
	epochs=EPOCHS, verbose=1)
## Training our network is initiated  where we call model.fit_generator , 
## supplying our data augmentation object, training/testing data, and the number of epochs we wish to train for.

# save the model to disk
print("[INFO] serializing network...")
model.save(args["model"])  ## handles serializing the model to disk so we later use our image classification without having to retrain it.

# plot the training loss and accuracy
LeNet.plot_model(model_details=H,path_to_save=args["plot"])
'''
plt.style.use("ggplot")
plt.figure()
N = EPOCHS
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy on Santa/Not Santa")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(args["plot"])
'''
## Using matplotlib, we build our plot and save the plot to disk using the --plot  command line argument which contains the path + filename.