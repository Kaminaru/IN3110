import cv2
import numpy as np

def numpy_color2sepia(filename,step=1):
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
        return

    #If 0% sepia, its just the normal image.
    if step == 0:
        return image
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB

    # To find shapes
    # H = image.shape[0]
    # W = image.shape[1]
    # C = image.shape[2]

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


    # # Stepless implementation - Does not work as expected
    # sepia = np.matrix([[0.393 + 0.607 * (1 - k), 0.769 - 0.769 * (1 - k), 0.189 - 0.189 * (1 - k)],
    #                     [0.349 - 0.349 * (1 - k), 0.686 + 0.314 * (1 - k), 0.168 - 0.168 * (1 - k)],
    #                     [0.272 - 0.349 * (1 - k), 0.534 - 0.534* (1 - k), 0.131 + 0.869 * (1 - k)]])

    # b = image[:, :, 0]*sepia.item((0, 0)) + image[:, :, 1]*sepia.item((0, 1)) + image[:, :, 2]*sepia.item((0, 2))
    # g = image[:, :, 0]*sepia.item((1, 0)) + image[:, :, 1]*sepia.item((1, 1)) + image[:, :, 2]*sepia.item((1, 2))
    # r = image[:, :, 0]*sepia.item((2, 0)) + image[:, :, 1]*sepia.item((2, 1)) + image[:, :, 2]*sepia.item((2, 2))

    if step != 1:
        sepia = (np.multiply(sepia, step) + np.multiply(image, (1-step)))

    sepia = sepia.astype("uint8")
    return sepia

# numpy_color2sepia()

# print("Average: ", timeit.timeit(numpy_color2sepia, number=3)/3)
