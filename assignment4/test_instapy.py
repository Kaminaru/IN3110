import instapy
import cv2
import numpy as np
from instapy.python_color2gray import python_color2gray
from instapy.python_color2sepia import python_color2sepia
from instapy.numba_color2gray import numba_color2gray
from instapy.numba_color2sepia import numba_color2sepia


def test_grayfilter():
    """ Testing gray scale implementation """
    for i in range(2): # check for two random made images
        # creates random image
                                            #    H   W  C
        # Creates a random np array with ints from 0 to 255
        newImage = np.random.randint(255, size=(200,250,3), dtype="uint8")
        cv2.imwrite("testGray.jpeg", newImage)


        withoutChanges = cv2.imread("testGray.jpeg")
        withoutChanges = cv2.cvtColor(withoutChanges, cv2.COLOR_BGR2RGB) # RGB

        for j in range(3):
            grayImage = None
            if j == 0: # numpy test
                grayImage = instapy.grayscale_image("testGray.jpeg")
            elif j == 1: # python test
                grayImage = python_color2gray("testGray.jpeg")
            else: # numba test
                grayImage = numba_color2gray("testGray.jpeg")
            # change to gray


            # To check shapes shapes  H W C
            assert withoutChanges.shape[0] == grayImage.shape[0]
            assert withoutChanges.shape[1] == grayImage.shape[1]
            assert withoutChanges.shape[2] == grayImage.shape[2]
            #Shold not have same variable name as the variables in loop.
            rand_x = np.random.randint(withoutChanges.shape[0])
            rand_y = np.random.randint(withoutChanges.shape[1])

            neededNum = withoutChanges[rand_x][rand_y][0]*0.21 + withoutChanges[rand_x][rand_y][1]*0.72 \
                        + withoutChanges[rand_x][rand_y][2]*0.07
            # checks each element in pixel
            assert int(neededNum) == int(grayImage[rand_x][rand_y][0])
            assert int(neededNum) == int(grayImage[rand_x][rand_y][1])
            assert int(neededNum) == int(grayImage[rand_x][rand_y][2])


def test_sepiafilter():
    """ Testing sepia filter implementation """
    for i in range(2): # check for two random made images
        # creates random image
                                           #     H   W  C
        # Creates a random np array with ints from 0 to 255
        newImage = np.random.randint(255, size=(200,250,3), dtype="uint8")
        cv2.imwrite("testSepia.jpeg", newImage)

        withoutChanges = cv2.imread("testSepia.jpeg")

        for j in range(3):
            sepiaImage = None
            if j == 0: # numpy test
                sepiaImage = instapy.sepia_image("testSepia.jpeg")
            elif j == 1: # python test
                sepiaImage = python_color2sepia("testSepia.jpeg")
            else: # numba test
                sepiaImage = numba_color2sepia("testSepia.jpeg")
            # To check shapes shapes  H W C
            assert withoutChanges.shape[0] == sepiaImage.shape[0]
            assert withoutChanges.shape[1] == sepiaImage.shape[1]
            assert withoutChanges.shape[2] == sepiaImage.shape[2]

            # choose random j and i
            rand_x = np.random.randint(withoutChanges.shape[0])
            rand_y = np.random.randint(withoutChanges.shape[1])

            neededRed = withoutChanges[rand_x][rand_y][0]*0.272 + withoutChanges[rand_x][rand_y][1]*0.534 \
                        + withoutChanges[rand_x][rand_y][2]*0.131
            if neededRed > 255:
                neededRed = 255
            neededGreen = withoutChanges[rand_x][rand_y][0]*0.349 + withoutChanges[rand_x][rand_y][1]*0.686 \
                        + withoutChanges[rand_x][rand_y][2]*0.168
            if neededGreen > 255:
                neededGreen = 255
            neededBlue = withoutChanges[rand_x][rand_y][0]*0.393 + withoutChanges[rand_x][rand_y][1]*0.769 \
                        + withoutChanges[rand_x][rand_y][2]*0.189
            if neededBlue > 255:
                neededBlue = 255
            # checks each element in pixel
            assert int(neededRed) == int(sepiaImage[rand_x][rand_y][0])
            assert int(neededGreen) == int(sepiaImage[rand_x][rand_y][1])
            assert int(neededBlue) == int(sepiaImage[rand_x][rand_y][2])

