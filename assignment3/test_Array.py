from Array import Array

def testGetitem():
    """
    Test __getitem__ function
    """
    try:
        ############################ 1D ############################
        my_array = Array((7,),2,3,1,0,5,6,9)
        assert my_array[-2] == 6
        assert my_array[0] == 2
        assert my_array[4] == 5
        assert my_array[-3] == 5
        ############################ 2D ############################
        my_array = Array((3,2),8,3,4,1,6,1)
        assert my_array[1][0] == 4
        assert my_array[1][1] == 1
        assert my_array[0][1] == 3
        assert my_array[2][0] == 6
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Wrong type of data. Please use numeric or boolean")

def testPrint():
    """
    Checks if __str__ function actually returns the nice string
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0)) == "[2, 3, 1, 0]"
        assert str(Array((4,),23.1,3.3,11.11,2.4)) == "[23.1, 3.3, 11.11, 2.4]"
        assert str(Array((4,),False,True,False,True)) == "[False, True, False, True]"
        assert str(Array((5,),1,3,3,5,1)) == "[1, 3, 3, 5, 1]"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1)) == "[[8, 3], [4, 1], [6, 1]]"
        assert str(Array((5,1),81,23,44,2,6)) == "[[81], [23], [44], [2], [6]]"
        assert str(Array((2,2),False,True,False,True)) == "[[False, True], [False, True]]"
        assert str(Array((3,3),0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)) == "[[0.0, 0.1, 0.2], [0.3, 0.4, 0.5], [0.6, 0.7, 0.8]]"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Wrong type of data. Please use numeric or boolean")


def testAddition():
    """
    Checks if __add__ function actually returns right value
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0) + Array((4,),2,3,1,5)) == "[4, 6, 2, 5]"
        assert str(Array((3,),True,False,False) + Array((3,),True,True,False)) == "[2, 1, 0]"
        assert str(Array((5,),2.1,3.0,1.123,0.0,1.2) + Array((5,),2.1,3.33,1.03,5.23,13.3)) == "[4.2, 6.33, 2.153, 5.23, 14.5]"
        assert str(Array((4,),2,3,1,0) + 3) == "[5, 6, 4, 3]"
        assert str(3 + Array((4,),2,3,1,0)) == "[5, 6, 4, 3]"  # but only if __radd__ is implemented! or else "None"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1) + Array((3,2),8,3,4,1,6,1)) == "[[16, 6], [8, 2], [12, 2]]"
        assert str(3 + Array((3,2),8,3,4,1,6,1)) == "[[11, 6], [7, 4], [9, 4]]"
        assert str(Array((2,2),1.5,2.0,4.0,1.5) + Array((2,2),1.5,2.0,4.0,2.0)) == "[[3.0, 4.0], [8.0, 3.5]]"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testSubtraction():
    """
    Checks if __sub__ function actually returns right value
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0) - Array((4,),2,3,1,5)) == "[0, 0, 0, -5]"
        assert str(Array((3,),True,False,False) - Array((3,),True,True,False)) == "[0, -1, 0]"
        assert str(Array((5,),2.1,3.0,1.2,0.0,1.2) - Array((5,),2.1,3.5,1.2,5.1,13.5)) == "[0.0, -0.5, 0.0, -5.1, -12.3]"
        assert str(Array((2,),4,65) - 2) == "[2, 63]"
        assert str(2 - Array((2,),4,65)) == "[-2, -63]" # but only if __rsub__ is implemented! or else "None"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1) - Array((3,2),8,3,4,1,6,1)) == "[[0, 0], [0, 0], [0, 0]]"
        assert str(3 - Array((3,2),8,3,4,1,6,1)) == "[[-5, 0], [-1, 2], [-3, 2]]"
        assert str(Array((2,2),1.5,2.0,4.0,1.5) - Array((2,2),1.5,2.0,4.0,2.0)) == "[[0.0, 0.0], [0.0, -0.5]]"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testMultiplication():
    """
    Checks if __mul__ function actually returns right value
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0) * Array((4,),2,3,1,5)) == "[4, 9, 1, 0]"
        assert str(Array((3,),True,False,False) * Array((3,),True,True,False)) == "[1, 0, 0]"
        assert str(Array((3,),2.0,0.5,10.4) * Array((3,),0.5,5.0,0.5)) == "[1.0, 2.5, 5.2]"
        assert str(Array((5,),1,2,3,4,5) * 10) == "[10, 20, 30, 40, 50]"
        assert str(10 * Array((4,),1,2,3,4)) == "[10, 20, 30, 40]" # but only if __rmul__ is implemented! or else "None"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1) * Array((3,2),8,3,4,1,6,1)) == "[[64, 9], [16, 1], [36, 1]]"
        assert str(3 * Array((3,2),8,3,4,1,6,1)) == "[[24, 9], [12, 3], [18, 3]]"
        assert str(Array((2,2),1.5,2.0,4.0,1.5) * Array((2,2),1.5,2.0,4.0,2.0)) == "[[2.25, 4.0], [16.0, 3.0]]"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testCompare():
    """
    Checks if __eq__ function actually returns right value
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0) == Array((4,),2,3,1,5)) == "False"
        assert str(Array((3,),True,False,False) == Array((3,),True,True,False)) == "False"
        assert str(Array((3,),2.0,0.5,10.4) == Array((3,),0.5,5.0,0.5)) == "False"
        assert str(Array((2,),1,2) == Array((2,),1,2)) == "True"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1) == Array((3,2),8,3,4,1,6,1)) == "True"
        assert str(Array((2,2),1.5,2.0,4.0,1.5) == Array((2,2),1.5,2.0,4.0,2.0)) == "False"
        assert str(Array((2,2),True,False,False,True) == Array((2,2),True,False,False,True)) == "True"
        assert str(Array((3,3),8,3,4,1,6,1,1,2,3) == Array((3,2),8,3,4,1,6,1)) == "False"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")


def testCompareIs():
    """
    Checks if is_equal function actually returns right value
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),2,3,1,0).is_equal(Array((4,),2,3,1,5))) == "[True, True, True, False]"
        assert str(Array((3,),True,False,False).is_equal(Array((3,),True,True,False))) == "[True, False, True]"
        assert str(Array((3,),2.0,0.5,10.4).is_equal(Array((3,),0.5,5.0,0.5))) == "[False, False, False]"
        assert str(Array((5,),1,2,1,4,1).is_equal(1)) == "[True, False, True, False, True]"
        ############################ 2D ############################
        assert str(Array((3,2),8,3,4,1,6,1).is_equal(Array((3,2),8,3,4,1,6,1))) == "[[True, True], [True, True], [True, True]]"
        assert str(Array((2,2),1.5,2.0,4.0,1.5).is_equal(Array((2,2),1.5,2.0,4.0,2.0))) == "[[True, True], [True, False]]"
        assert str(Array((2,2),True,False,False,True).is_equal(Array((2,2),True,False,False,True))) == "[[True, True], [True, True]]"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testMean():
    """
    Finds out the mean of the data in array
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),1,2,3,4).mean()) == "2.5"
        assert str(Array((3,),2.0,0.5,10.4).mean()) == "4.3"
        assert str(Array((2,),5,25).mean()) == "15.0"
        ############################ 2D ############################
        # wasn't sure if I need to calculate mean for all the numbers of for each row
        # so i just did for all numbers form all rows
        assert str(Array((4,2),1,2,3,4,1,3,4,5).mean()) == "2.875"
        assert str(Array((3,1),2.0,0.5,10.4).mean()) == "4.3"
        assert str(Array((2,2),5,25,3,4).mean()) == "9.25"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testVariance():
    """
    Finds out the variance of the data in array
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),1,2,3,4).variance()) == "1.25"
        assert str(Array((3,),2.0,0.5,10.4).variance()) == "18.98"
        assert str(Array((2,),5,25).variance()) == "100.0"
        ############################ 2D ############################
        assert str(Array((4,2),1,2,3,4,1,3,4,5).variance()) == "1.859375"
        assert str(Array((3,1),2.0,0.5,10.4).variance()) == "18.98"
        assert str(Array((2,2),5,25,3,4).variance()) == "83.1875"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")

def testMinElem():
    """
    Finds out smallest value in the array
    """
    try:
        ############################ 1D ############################
        assert str(Array((4,),1,2,3,4).min_element()) == "1.0"
        assert str(Array((3,),2.0,0.5,10.4).min_element()) == "0.5"
        assert str(Array((7,),5,25,3,1,4,5,0).min_element()) == "0.0"
        ############################ 2D ############################
        assert str(Array((4,2),1,2,3,4,6,3,0,10).min_element()) == "0.0"
        assert str(Array((3,),2.0,0.5,10.4).min_element()) == "0.5"
        assert str(Array((7,),5,25,3,1,4,5,0).min_element()) == "0.0"
    except ValueError:
        print("Eather number of values does not fit with the shape or values are not all of the same type!")
    except Exception:
        print("Something else went wrong")
