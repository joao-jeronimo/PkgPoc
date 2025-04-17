Python module that contains scripts and libraries, so of them calling
foreign functions written in C.

To install:
    ./setup.py install
To smoke-test:
    pushd .. ; python3 -c "import samplepythonlibmodules" ; samplepythonprogram.py thongs ; samplepythonprogram.py squaredoubles8.1 ; samplepythonprogram.py square7 ; popd
To uninstall:
    pip uninstall sample-pythonforeignlib
