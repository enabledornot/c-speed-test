# C Speed Test
This repository contains programs designed to compare the speed of integer operations and floating point operations in the C programming language

It was designed to be used under a linux environment since compiling c code is easier and linux has access to the ```time``` function for more accurate timing

# Installing Python and Pip
 - If you do not already have python and pip installed you can install them on ubuntu with the following commands:
```
sudo apt install python3
sudo apt install python3-pip
```

# Building Binaries
 - **Note** must be done on a linux machine
 - **Note** depending on how python is installed you might need to modify the ```generate.sh``` file to call ```python``` instead of ```python3```
 - Building the binaries used do the testing is as easy as running ```sh generte.sh``` from this repository

# Running Tests
- **Note** you must have tqdm installed in order for the ```bulktest.py``` program to function.  To install tqdm run ```pip install tqdm```
- **Note** If python is not accessible through the ```python3``` you may need to replace it with ```python```
- To run the tests run ```python3 bulktest.py numberOfTries``` replacing numberOfTries with the number of executions you want the program to go through before printing out the data
