import cv2

def numpy_color2gray(filename):
    '''
    Applies a gray filter using numpy.
    Args: 
        image: numpy array. input image.

    Return:
        gray: numpy arr that is a image with the filters applied.
    '''
    try:
        image = cv2.imread(filename)  # BGR (not RGB)
        # To find shapes
        # H = image.shape[0]
        # W = image.shape[1]
        # C = image.shape[2]
    except Exception:
        print("No such file")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB
    image[:, :, :] = image[:, :, 0:1]*0.21 + image[:, :, 1:2]*0.72 + image[:, :, 2:3]*0.07

    image = image.astype("uint8")
    # cv2.imwrite('rain_grayscale.jpeg', image)

    return image

# numpy_color2gray("rain.jpg")

# print("Average: ", timeit.timeit(numpy_color2gray, number=1000)/1000)
