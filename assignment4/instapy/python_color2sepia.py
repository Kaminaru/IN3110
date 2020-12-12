import cv2

def python_color2sepia(filename,step=1):
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

    sepia = image.copy()

    #  = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB
    # for i in range(len(image)):
    #     for j in range(len(image[i])):
    #         red = image[i][j][0]*0.272 + image[i][j][1]*0.534 + image[i][j][2]*0.131
    #         if(red > 255):
    #             red = 255
    #         green = image[i][j][0]*0.349 + image[i][j][1]*0.686 + image[i][j][2]*0.168
    #         if(green > 255):
    #             green = 255
    #         blue = image[i][j][0]*0.393 + image[i][j][1]*0.769 + image[i][j][2]*0.189
    #         if(blue > 255):
    #             blue = 255
    #         image[i][j] = (red, green, blue)

    # Stepless implementation
    for i in range(len(sepia)):
        for j in range(len(sepia[i])):
            red = sepia[i][j][0]*(0.272) + sepia[i][j][1]*(0.534) + sepia[i][j][2]*(0.131)
            red = (red * step + image[i][j][2] * (1-step))
            if(red > 255):
                red = 255
            green = sepia[i][j][0]*(0.349) + sepia[i][j][1]*(0.686) + sepia[i][j][2]*(0.168)
            green = (green * step + image[i][j][1] * (1-step))
            if(green > 255):
                green = 255
            blue = sepia[i][j][0]*(0.393) + sepia[i][j][1]*(0.769) + sepia[i][j][2]*(0.189)
            blue = (blue * step + image[i][j][0] * (1-step))
            if(blue > 255):
                blue = 255
            sepia[i][j] = (red, green, blue)



    sepia = sepia.astype("uint8")
    return sepia

# python_color2sepia()

# print("Average: ", timeit.timeit(python_color2sepia, number=3)/3)
