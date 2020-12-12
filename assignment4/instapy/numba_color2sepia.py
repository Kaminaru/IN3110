import cv2
import numpy as np
from numba import jit

def numba_color2sepia(filename,step=1):
    """
        Function that takes filename and k value for sephia filter level.
        And returns image (3D array) in sepia filter

        Args:
            filename: string. File to be applied filter to
            step: float. How many percent the filter is to be applied.
        Returns:
            sepia: numpy array of the image with filters applied
    """
    try:
        image = cv2.imread(filename)  # BGR (not RGB)
    except Exception:
        print("No such file")
        return np.array([])
    
    if step == 0:
        return image


    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB

    sepia = numpyCal(image)

    #Last implementation of stepless sepia didnt work. 
    #Here we take the two images and determenate how much of 
    #each we want in the stepless sepia filter.
    if step != 1:
        sepia = (np.multiply(sepia, step) + np.multiply(image, (1-step)))

    sepia = sepia.astype("uint8")
    # cv2.imshow('rain.jpg',image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite('rain_sepia.jpeg', image)
    return sepia

@jit
def numpyCal(image):
    sepia = image.copy()

    b = sepia[:, :, 0]*0.393 + sepia[:, :, 1]*0.769 + sepia[:, :, 2]*0.189
    g = sepia[:, :, 0]*0.349 + sepia[:, :, 1]*0.686 + sepia[:, :, 2]*0.168
    r = sepia[:, :, 0]*0.272 + sepia[:, :, 1]*0.534 + sepia[:, :, 2]*0.131

    b = np.minimum(b, 255) # choosing the smallest number
    g = np.minimum(g, 255)
    r = np.minimum(r, 255)

    sepia[:,:,0] = r
    sepia[:,:,1] = g
    sepia[:,:,2] = b
    return sepia
# numba_color2sepia()

# print("Average: ", timeit.timeit(numba_color2sepia, number=500)/500)
