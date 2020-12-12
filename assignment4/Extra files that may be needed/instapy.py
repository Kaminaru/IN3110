#!/usr/bin/env python3
import argparse
import cv2
import os
from instapy.python_color2gray import python_color2gray
from instapy.python_color2sepia import python_color2sepia
from instapy.numpy_color2gray import numpy_color2gray
from instapy.numpy_color2sepia import numpy_color2sepia
from instapy.numba_color2gray import numba_color2gray
from instapy.numba_color2sepia import numba_color2sepia

parser = argparse.ArgumentParser(description="Easy calculator")
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='The file name of file to apply filter to')

group1 = parser.add_mutually_exclusive_group() # gray or sepia filter group
group1.add_argument('-se', '--sepia', action = 'store_true', help='Select sepia filter')
group1.add_argument('-g', '--gray', action = 'store_true', help='Select gray filter')

parser.add_argument('-sc', '--scale', type=float, metavar='', help='Scale factor to resize image')
parser.add_argument('-i', '--implement', type=str, metavar='', help='Choose the implement')
parser.add_argument('-o', '--out', type=str, metavar='', help='The output filename')

args = parser.parse_args()

def sepia(input_filename):
    image = None
    if args.implement == "python":
        image = python_color2sepia(input_filename)
    elif args.implement == "numba":
        image = numba_color2sepia(input_filename)
    else: # if numpy (or if it is nothing, it will do numpy too)
        image = numpy_color2sepia(input_filename)

    if args.scale: # if scale is given
        image = cv2.resize(image, (0, 0), fx=args.scale, fy=args.scale)

    if args.out: # if there is given output file name
        path = input("Write path (in form: D:/Images/Changed or Changed (if you are in the Images folder))")
        cv2.imwrite(os.path.join(path , args.out),image)

def gray(input_filename):
    image = None
    if args.implement == "python":
        image = python_color2gray(input_filename)
    elif args.implement == "numba":
        image = numba_color2gray(input_filename)
    else: # if numpy (or if it is nothing, it will do numpy too)
        image = numpy_color2gray(input_filename)

    if args.scale: # if scale is given
        image = cv2.resize(image, (0, 0), fx=args.scale, fy=args.scale)

    if args.out: # if there is given output file name
        path = input("Write path (in form: D:/Images/Changed or Changed (if you are in the Images folder))")
        cv2.imwrite(os.path.join(path , args.out),image)


if __name__ == '__main__':
    if args.sepia: # sepia filter is choosen (Don't need to check if gray arg is on.
                                            # Because one group can have only one arg on)
        sepia(args.file)
    elif args.gray: # gray filter is choosen
        gray(args.file)
    else:
        print("Please choose the filter")
