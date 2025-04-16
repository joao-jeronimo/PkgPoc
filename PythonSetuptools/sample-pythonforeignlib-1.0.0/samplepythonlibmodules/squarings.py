import ctypes

### Importing the object:
my_functions = ctypes.CDLL("./my_functions.so")
my_functions.square_doubles.restype = ctypes.c_double

def from_c_square(number):
    return my_functions.square(number)

def from_c_square_doubles(number):
    return my_functions.square(ctypes.c_double(number))
