from ctypes import *
from jnius import autoclass
import pathlib

# Setting Working DIR here for any os.
WORK_DIR = pathlib.Path().absolute()

# locating C dll file in working dir.
LIBPATH = WORK_DIR / "libHES_SO.so"

# load the c library
lib1 = CDLL(LIBPATH)

# Initializing Java class
DLMSParsing = autoclass('DLMSParsing')

# Creating object DLMSParsing class
java_parser = DLMSParsing()


if __name__ == "__main__":
    
    abc = bytes([1])
    # data = bytearray([1,2,3,4,5])
    ret_value = lib1.apiDLMSENGINElib(
        # byref(c_int(abc[0])),
        # byref(c_int(abc[0])),
        # byref(c_int(abc[0])),
        # byref(c_int(abc[0])),
        # byref(c_ubyte(1)),
        # byref(c_ubyte(1)),
        # byref(c_ubyte(1)),
        # byref(c_ubyte(1)),
        # c_char_p(abc),
        # c_char_p(abc),
        # c_char_p(abc),
        # c_char_p(abc),
        c_buffer(abc),
        c_buffer(abc),
        c_buffer(abc),
        c_buffer(abc),
        c_int(1)
    )
    print(f'{ret_value=}')
    if ret_value == 0:
        print("C DLL load Sucessfully")
    
    CSVstatus = 0
    CSVstatus = java_parser.CreateCSVorDB(20)
    print(f'{CSVstatus=}')
    if CSVstatus:
        print("JAVA DLL load Sucessfully.")
