import cv2
from numba import jit


def numba_color2gray(filename):
    '''
    Applies a gray filter using numba.
    Args: 
        image: numpy array. input image.

    Return:
        image: numpy arr that is a image with the filters applied.
    '''
    try:
        image = cv2.imread(filename)  # BGR (not RGB)
    except Exception:
        print("No such file")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB

    image = numpyCal(image)

    image = image.astype("uint8")
    # cv2.imwrite('rain_grayscale.jpeg', image)
    return image


@jit(nopython=True)
def numpyCal(image):
    """ numpy calculations """
    image[:, :, :] = image[:, :, 0:1]*0.21 + image[:, :, 1:2]*0.72 + image[:, :, 2:3]*0.07
    return image


# numba_color2gray()
# print("Average: ", timeit.timeit(numba_color2gray, number=400)/400)
