import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "                           # s = "La cuill (re n'existe pas"
lib.print_python_string(s)
s = "lib.print_python_string(s)
s = ")
 s = b"The spoon does not exist"
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value:                        #   type: compact unicode object
  length: 24
  value: La cuill (re n'existe pas
                                                 [.] string object info
                                                 type: compact unicode object
                                                 length: 5
                                                 value:   type: compact unicode object
  length: 14
  value:
                                                   [ERROR] Invalid String Object
