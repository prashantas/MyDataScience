'''
https://stackoverflow.com/questions/28570058/running-command-line-commands-within-pycharm
Press Alt+F12 to open terminal within PyCharm, then write in the command you wish to run and press enter.
In your case:

Press Alt+F12
Type python Test.py GET /feeds
Press Enter
'''

# -*- coding: utf-8 -*-


## https://deeplearningsandbox.com/how-to-build-an-image-recognition-system-using-keras-and-tensorflow-for-a-1000-everyday-object-559856e04699
import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt
import argparse
import sys
import requests
from io import BytesIO
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
model = ResNet50(weights='imagenet')
## model = VGG16(weights='imagenet', include_top=False)
## if we use VGG16 then include_top=False means not to include the Fully Connected layer. it will include only
## Convolution layer

def predict(model, img, target_size, top_n=3):
    """Run model prediction on image
    Args:
        model: keras model
        img: PIL format image
        target_size: (width, height) tuple
        top_n: # of top predictions to return
    Returns:
        list of predicted labels and their probabilities
    """
    print('img.size=',img.size)
    if img.size != target_size:
        img = img.resize(target_size)
        
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return decode_predictions(preds,top=top_n)[0]

'''
Note that to use the ResNet50 architecture, target_size must equal (224, 224). Many CNN architectures have a fixed input size and
ResNet50 is one such architecture, where the inventors used a fixed size input of (224, 224).

image.img_to_array: converts a PIL format image to a numpy array

np.expand_dims: converts our (3, 224, 224) size image to (1, 3, 224, 2 24). The reason for this is that the model.predict function
requires a 4 dimensional array as input, where the 4th dimension corresponds to the batch size. That means, if we wanted to, 
we could classify multiple images at once.

preprocess_input: zero-centers our image data using the mean channel values from the training dataset. This is an extremely important
step that, if skipped, will cause all the predicted probabilities to be incorrect. This mean centering is what’s called data 
normalization, a fundamental concept in machine learning.

model.predict: runs inference on our data batch and returns predictions

decode_predictions: takes the coded labels associated with model.predict and returns human-readable labels from the ImageNet ILSVRC set.

The keras.applications module provides 4 off-the-shelf architectures: ResNet50, InceptionV3, VGG16, VGG19, XCeption. We arbitrarily 
chose ResNet50, but you are free to swap that out with any of the other off-the-shelf architectures.
Checkout https://keras.io/applications/ for additional information and references.

'''

"""
Plotting
We can use matplotlib to print the output in a horizontal bar graph like so:
"""

def plot_preds(image, preds):  
  """Displays image and the top-n predicted probabilities 
     in a bar graph  
  Args:    
    image: PIL image
    preds: list of predicted labels and their probabilities  
  """  
  #image
  plt.imshow(image)
  plt.axis('off')
  
  #bar graph
  plt.figure()  
  order = list(reversed(range(len(preds))))  
  bar_preds = [pr[2] for pr in preds]
  labels = (pr[1] for pr in preds)
  plt.barh(order, bar_preds, alpha=0.5)
  plt.yticks(order, labels)
  plt.xlabel('Probability')
  plt.xlim(0, 1.01)
  plt.tight_layout()
  plt.show()
  

if __name__=="__main__":
  a = argparse.ArgumentParser()
  a.add_argument("--image", help="path to image")
  a.add_argument("--image_url", help="url to image")
  args = a.parse_args()
if args.image is None and args.image_url is None:
    a.print_help()
    sys.exit(1)
if args.image is not None:
    #img = image.open(args.image)
    img = image.load_img(args.image)
    pred = predict(model, img, target_size=(224,224))
    print('pred::',pred)
    plot_preds(img,pred)
if args.image_url is not None:
    response = requests.get(args.image_url)
    #img = image.open(BytesIO(response.content))
    img = image.load_img(BytesIO(response.content))
    plot_preds(img, predict(model, img, target_size=(224,224)))
    
"""
Main
In order to have this command line usage:
1. python Resnet50.py --image African_Bush_Elephant.jpg
2. python Resnet50.py --image_url http://i.imgur.com/wpxMwsR.jpg
"""
