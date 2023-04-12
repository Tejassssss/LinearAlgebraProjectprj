#Imports
import numpy as np
from PIL import Image

def image_transform(image_np, linear_transform):
  # Get the dimensions of the image
  height, width, channels = image_np.shape

  # Define the center
  center_x = width / 2
  center_y = height / 2

  # Loop through each pixel in the image and apply the transformation
  transformed_image = np.zeros_like(image_np)

  for y in range(height):
      for x in range(width):
          # Translate the pixel to the origin
          translated_x = x - center_x
          translated_y = -(y - center_y)
          
          # Apply the transformation: matrix vector multiplication
          transformed_x, transformed_y = linear_transform@np.array([translated_x, translated_y])
          
          # Translate the pixel back to its original position
          transformed_x += center_x
          transformed_y = - transformed_y + center_y
          
          # Round the pixel coordinates to integers
          transformed_x = int(round(transformed_x))
          transformed_y = int(round(transformed_y))
          
          # Copy the pixel to the transformed image
          if (transformed_x >= 0 and transformed_x < width and
              transformed_y >= 0 and transformed_y < height):
              transformed_image[transformed_y, transformed_x] = image_np[y, x]

  return transformed_image

if __name__ == "__main__":
    #Read in the image
    image0 = Image.open('linalgphoto.jpg',mode='r')
    image0_np = np.array(image0)

    #check correct size.
    print("The shape of image0_np is "+ str(image0_np.shape))

    half = np.array([
    [0.5, 0],
    [0, 0.5]])
    image1_np = image_transform(image0_np, half)
    image1 = Image.fromarray(image1_np)
    image1.show()

    ytwox = np.array([
    [-0.6, 0.8],
    [0.8, 0.6]])
    image2_np = image_transform(image1_np,ytwox)
    image2 = Image.fromarray(image2_np)
    image2.show()

    ynegativehalfx = np.array([
    [0.6, -0.8],
    [-0.8, -0.6]])
    image3_np = image_transform(image2_np,ytwox)
    image3 = Image.fromarray(image3_np)
    image3.show()

    Image.fromarray(image_transform(image1_np,ytwox@half)).show()

    inverseT = np.array([
    [-1.2, 1.6],
    [1.6, 1.2]])
    Image.fromarray(image_transform(image3_np,inverseT)).show()

    inverseTwo = np.array([
    [-2, 0],
    [0, -2]])
    image4_np = image_transform(image1_np,inverseTwo)
    image4 = Image.fromarray(image4_np)
    image4.show()

    print(image1)
