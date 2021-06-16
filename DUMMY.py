from ctypes import *
from jnius import autoclass
import pathlib

# Setting Working DIR here for any os.
WORK_DIR = pathlib.Path().absolute()

# locating C dll file in working dir.
LIBPATH = WORK_DIR / "libDUMMY.so"

# load the c library
dummy = CDLL(LIBPATH)


if __name__ == "__main__":
    
    num_array = (c_int * 5)(1,2,3,4,5)
    text = bytes("SHUBHAM".encode("ASCII"))

    dummy.printCharVal(c_char_p(text), c_int(7))
    dummy.printIntVal(pointer(num_array), c_int(5))
