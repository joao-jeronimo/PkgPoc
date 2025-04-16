#!/bin/env python3
import sys
import samplepythonlibmodules

if sys.argv[1] == 'things':
    samplepythonlibmodules.printhings()
elif sys.argv[1] == 'thongs':
    samplepythonlibmodules.printhongs()
elif sys.argv[1] == 'square7':
    samplepythonlibmodules.from_c_square(7)
elif sys.argv[1] == 'squaredoubles8.1':
    samplepythonlibmodules.from_c_square_doubles(8.1)
else:
    print(f"Cannot print {sys.argv[1]}. I can only print 'things', 'thongs', 'square7' and 'squaredoubles8.1'.")
