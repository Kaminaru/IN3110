import cv2

def python_color2gray(filename):
    '''
    Applies a gray filter using numba.
    Args: 
        image: numpy array. input image.

    Return:
        gray: numpy arr that is a image with the filters applied.
    '''
    try:
        image = cv2.imread(filename)  # BGR (not RGB)
    except Exception:
        print("No such file")
        return
    # To find shapes
    # H = image.shape[0]
    # W = image.shape[1]
    # C = image.shape[2]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB
    for i in range(len(image)):
        for j in range(len(image[i])):
            tmp = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07
            image[i][j] = (tmp, tmp, tmp)

    # cv2.imshow('rain.jpg',image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = image.astype("uint8")
    # cv2.imwrite('rain_grayscale.jpeg', image)
    return image

# python_color2gray()

# print("Average: ", timeit.timeit(python_color2gray, number=3)/3)
