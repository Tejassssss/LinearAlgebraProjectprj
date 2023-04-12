#Imports
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cv2 

def displayImage(image):
    plt.imshow(image, interpolation='nearest')
    plt.show()

def halfScale(image):
    scaled_image = image[::2, ::2]

    return scaled_image

if __name__ == "__main__":
    #Read in the image
    image0 = Image.open('linalgphoto.jpg',mode='r')
    image0_np = np.array(image0)

    #check correct size. Should be height*width*3
    print(image0_np.shape)

    image1 = halfScale(image0_np)
    print(image1[0][0])
    displayImage(image1)
    displayImage(image0_np)
    print(image1)