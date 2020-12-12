from .numpy_color2gray import numpy_color2gray
from .numpy_color2sepia import numpy_color2sepia

import cv2
import os

def grayscale_image(input_filename, output_filename=None):
    """
        Takes input filename, makes this image gray and return its to a caller
        If output filename is given, saves it in that location.
        Here I guess that the output_filename is also just a name for file
    """
    image = numpy_color2gray(input_filename)
    if output_filename: # check if otuput loaction is given
        path = input("Write path (in form: D:/Images/Changed or Changed (if you are in the Images folder))")
        cv2.imwrite(os.path.join(path , output_filename),image)
    return image

def sepia_image(input_filename, output_filename=None):
    """
        Takes input filename, changes this image to sepia and return its to a caller
        If output filename is given, saves it in that location.
        Here i guess that the output_filename is also "path"
    """
    image = numpy_color2sepia(input_filename, 1)
    if output_filename:
        path = input("Write path (in form: D:/Images/Changed or Changed (if you are in the Images folder))")
        cv2.imwrite(os.path.join(path , output_filename),image)
    return image
