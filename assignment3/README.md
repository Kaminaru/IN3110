# Mandatory Assignment 3 (IN3110)

# Basic Python Programming

1. wc.py file takes filename as argument and finds out number of lines, words and
characters in the file and prints it out.
2. Array.py is a array class that have different magical functions
3. test_Array.py is a test program for array class.



Usage:
  wc.py file:<br />
    - To run the program you need one argument (file name)<br />
    
      Possible argument:
                          filename.py
                          \*.py
                          \*    

      How to run:
                  python wc.py filename.py     (for only one file)
                  python wc.py \*.py            (for only .py files)
                  python wc.py \*               (for all files in the directory)
                  ./wc filename.py             

      Output:
              Program prints out: a b c fn
                          Where:
                          a = number of lines in the file
                          b = number of words in the file
                          c = number of characters in file
                          fn = filename

  Array_test.py
    - You don't need any arguments to run this file <br />
    You can either run it normaly as:  python Array_test.py <br />
    Or you can use pytest (if it's installed on your PC): pytest
