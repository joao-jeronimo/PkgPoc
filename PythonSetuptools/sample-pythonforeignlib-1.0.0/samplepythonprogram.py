#!/bin/env python3
import sys
import samplepythonlibmodules

if sys.argv[1] == 'things':
    samplepythonlibmodules.printhings()
elif sys.argv[1] == 'thongs':
    samplepythonlibmodules.printhongs()
else:
    print(f"Cannot print {sys.argv[1]}. I can only print 'things' and 'thongs'.")
