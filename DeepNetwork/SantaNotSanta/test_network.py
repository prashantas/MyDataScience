# USAGE
# python test_network.py --model santa_not_santa.model --image examples/santa_01.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
## Take special notice of the load_model  method — this function will enable us to load our serialized
## Convolutional Neural Network (i.e., the one we just trained in the previous section) from disk.

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
## We require two command line arguments: our --model  and a input --image (i.e., the image we are going to classify).

# load the image
image = cv2.imread(args["image"])
print("image shape after cv2.imread:", image.shape)
orig = image.copy()
## We load the image  and make a copy of it on Lines .
## The copy allows us to later recall the original image and put our label on it.

# pre-process the image for classification
image = cv2.resize(image, (28, 28))
print("image shape after cv2.resize(image, (28,28):", image.shape)
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
print("image shape np.expand_dims:", image.shape)
## handling scaling our image to the range [0, 1], converting it to an array,
## and addding an extra dimension
## we train/classify images in batches with CNNs. Adding an extra dimension to the array
## via np.expand_dims  allows our image to have the shape (1, width, height, 3) , assuming channels last ordering.
## If we forget to add the dimension, it will result in an error when we call model.predict  down the line.

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

# classify the input image
print("model.predict(image)::", model.predict(image))
## output :: model.predict(image):: [[ 0.03175658  0.96824336]]
(notSanta, santa) = model.predict(image)[0]


## And finally, we’ll use our prediction to draw on the orig  image copy and display it to the screen:
# build the label
label = "Santa" if santa > notSanta else "Not Santa"
proba = santa if santa > notSanta else notSanta
label = "{}: {:.2f}%".format(label, proba * 100)

# draw the label on the image
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

# show the output image
cv2.imshow("Output", output)
cv2.waitKey(0)

## We build the label (either “Santa” or “Not Santa”)  and then choose the corresponding probability value on Line 52.
## The label  and  proba are used on Line 52 to build the label text to show at the image as you’ll see in the top left corner of the output images below.
##We resize the images to a standard width to ensure it will fit on our screen, and then put the label text on the image (Lines 40-42).

## Finally, on Lines 45, we display the output image until a key has been pressed (Line 46).