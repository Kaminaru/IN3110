class Array:
    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        if (len(shape) == 1 and len(values) != shape[0]): # 1D array
            raise ValueError # The number of values does not fit with the shape
        elif(len(shape) == 2 and len(values) != shape[0]*shape[1]): # 2D array
            raise ValueError # The number of values does not fit with the shape

        self.shape = shape
        # checks if first element is boolean or int
        t = values[0]
        if(isinstance(t, int) or isinstance(t, bool) or isinstance(t, float)):
            for i in range(1,len(values)): # goes from second element (we have checked first one)
                if not (type(values[0]) == type(values[i])):
                    raise ValueError # The values are not all of the same type
                self.values = values
        else:
            raise Exception # Wrong type of data. Please use numeric or boolean


    # Gets needed item from array
    # returns int, float or boolean
    def __getitem__(self,index):
        # This one was a little bit tricky to figure out for 2D, but I got it somehow:
        jump = 0; # jump between rows (stays 0 for 1D)
        if(index < self.shape[0]): # if it is in the array boundaries
            if(len(self.shape) == 2): # if 2D
                jump = index*self.shape[1]
                tmpTuple = self.values[jump:jump+self.shape[1]] # takes needed row from 2D array
                return Array((self.shape[1],),*tmpTuple) # sends new "1D array" to getitem
            elif(len(self.shape) == 1): # if 1D
                return self.values[index]
        else:
            print("Index is out of boundaries")
            return None

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        if(len(self.shape) == 1): # 1D
            output = "["
            for i in range(len(self.values)):
                output += str(self.values[i])
                if(i != len(self.values)-1): # so won't add ", " after last element
                    output += ", "
            output += "]"
            return output
        elif(len(self.shape) == 2): # 2D
            output = "["
            start = 0;
            # rowSize = self.shape[1]
            for i in range(self.shape[0]): # goes through all rows
                output += "["
                for j in range(self.shape[1]): # goes through columns
                    output += str(self.values[j+start])
                    if(j != self.shape[1]-1): # so won't add ", " after last element
                        output += ", "
                start += self.shape[1] # so it goes to "next" row
                output += "]"
                if(i != self.shape[0]-1): # so won't add ", " after last element
                    output += ", "
            output += "]"

            return output

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if(isinstance(other, int) or isinstance(other, float)): # so we will use number and not array
            # Here i would put check if other is float or int, and compare it with
            # type for the first element of self.values. But python will change type
            # to float automaticly if we will multiply int with float
            # So thats why I don't really need to implement solution for that

            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = self.values[i] + other
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        elif(self.shape[0] == other.shape[0]): # they need to have same shape
            # to make sure that I am not doing operation with not equal nxm 2D arrays
            if(len(other.shape) == 2 and self.shape[1] != other.shape[1]):
                print("Not same 2D array dimensions")
                return NotImplemented
            if(type(self.values[0]) == type(other.values[0])): # must have same type
                tempTuple = () # tuple ()
                for i in range(len(self.values)):
                    sum = self.values[i] + other.values[i]
                    tempTuple += (sum,)
                return Array(self.shape, *tempTuple)
            else:
                return NotImplemented
        else:
            return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        # I could also just call for __add__ function from this function
        # return self.__add__(other)

        # The code is shorter than __add__ because we know if __radd__ is called
        # that means that we add a different class (in our case int and float)
        # In other words I know that other is a int or float
        if(isinstance(other, int) or isinstance(other, float)):
            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = self.values[i] + other # element wise add
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        else:
            return NotImplemented

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if(isinstance(other, int) or isinstance(other, float)): # so we will use number and not array
            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = self.values[i] - other
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        elif(self.shape[0] == other.shape[0]): # they need to have same shape
            # to make sure that I am not doing operation with not equal nxm 2D arrays
            if(len(other.shape) == 2 and self.shape[1] != other.shape[1]):
                print("Not same 2D array dimensions")
                return NotImplemented
            if(type(self.values[0]) == type(other.values[0])): # must have same type
                tempTuple = () # tuple ()
                for i in range(len(self.values)):
                    sum = self.values[i] - other.values[i]
                    tempTuple += (sum,)
                return Array(self.shape, *tempTuple)
            else:
                return NotImplemented
        else:
            return NotImplemented


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        # The code is shorter than __sub__ because we know if __rsub__ is called
        # that means that we add a different class (in our case int and float)
        # In other words I know that other is a int or float
        if(isinstance(other, int) or isinstance(other, float)):
            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = other - self.values[i]
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        else:
            return NotImplemented

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if(isinstance(other, int) or isinstance(other, float)): # so we will use number and not array
            # Here i would put check if other is float or int, and compare it with
            # type for the first element of self.values. But python will change type
            # to float automaticly if we will multiply int with float
            # So thats why I don't really need to implement solution for that

            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = self.values[i] * other
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        elif(self.shape[0] == other.shape[0]): # they need to have same shape
            # to make sure that I am not doing operation with not equal nxm 2D arrays
            if(len(other.shape) == 2 and self.shape[1] != other.shape[1]):
                print("Not same 2D array dimensions")
                return NotImplemented
            if(type(self.values[0]) == type(other.values[0])): # must have same type
                tempTuple = () # tuple ()
                for i in range(len(self.values)):
                    sum = self.values[i] * other.values[i]
                    tempTuple += (sum,)
                return Array(self.shape, *tempTuple)
            else:
                return NotImplemented
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Here the code is shorter than __mul__ for the same reason as for
        # __radd__ and __rsub__
        if(isinstance(other, int) or isinstance(other, float)):
            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                sum = self.values[i] * other
                tempTuple += (sum,)
            return Array(self.shape, *tempTuple)
        else:
            return NotImplemented

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """
        if(self.shape[0] == other.shape[0]): # they need to have same shape
            if(type(self.values[0]) == type(other.values[0])): # must have same type
                # extra check for 2D arrays
                if(len(other.shape) == 2 and self.shape[1] != other.shape[1]):
                    return False
                for i in range(len(self.values)):
                    if(self.values[i] != other.values[i]):
                        return False
                return True
            else:
                return False # unexpected type
        else:
            return False # not same shape

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if(isinstance(other, int) or isinstance(other, float)): # so we will use number and not array
            tempTuple = () # tuple ()
            for i in range(len(self.values)):
                if(self.values[i] == other):
                    tempTuple += (True,)
                else:
                    tempTuple += (False,)
            return Array(self.shape, *tempTuple)
        elif(self.shape[0] == other.shape[0]): # they need to have same shape
            # to make sure that I am not doing operation with not equal nxm 2D arrays
            if(len(other.shape) == 2 and self.shape[1] != other.shape[1]):
                print("Not same 2D array dimensions")
                return NotImplemented
            if(type(self.values[0]) == type(other.values[0])): # must have same type
                tempTuple = () # tuple ()
                for i in range(len(self.values)):
                    if(self.values[i] == other.values[i]):
                        tempTuple += (True,)
                    else:
                        tempTuple += (False,)
                return Array(self.shape, *tempTuple)
            else:
                return NotImplemented # not the same type
        else:
            raise ValueError

    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        if(isinstance(self.values[0], int) or isinstance(self.values[0], float)):
            sum = 0
            for el in self.values:
                sum += el
            return float(sum/len(self.values))
        else:
            return NotImplemented # if we didn't got int or float type in array

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        if(isinstance(self.values[0], int) or isinstance(self.values[0], float)):
            mean = self.mean()
            sqDiff = 0
            for el in self.values:
                sqDiff += ((el - mean)**2)
            return sqDiff / len(self.values)
        else:
            return NotImplemented # if we didn't got int or float type in array


    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        if(isinstance(self.values[0], int) or isinstance(self.values[0], float)):
            minElem = self.values[0] # we can just "say" that first element is smallest
            for el in self.values:   # for each element in values
                if(el < minElem):
                    minElem = el
            return float(minElem)
        else:
            return NotImplemented # if we didn't got int or float type
