# A Python Drawing Program
A simple drawing program with input and output text files

# Brief Overview and Context
This program can be used to explore how Cait might approach different programming challenges.

# Command List supported in this version

```
Command 		Description
C w h           Create a new canvas of width w and height h.
L x1 y1 x2 y2   Create a new line from (x1,y1) to (x2,y2) using 'x'. Only supports 
                horizontal or vertical lines.
R x1 y1 x2 y2   Create a new rectangle whose upper left corner is (x1,y1) and (x2,y2) is the
                lower right corner.
B x y c         Fill the entire area connected to (x,y) with "colour" c.
                Same as that of the "bucket fill" tool in paint programs.
``` 

# Examples
```
C 20 4
----------------------
|                    |
|                    |
|                    |
|                    |
----------------------

L 1 2 6 2
----------------------
|                    |
|xxxxxx              |
|                    |
|                    |
----------------------

L 6 3 6 4
----------------------
|                    |
|xxxxxx              |
|     x              |
|     x              |
----------------------

R 16 1 20 3
----------------------
|             xxxxxx |
|xxxxxx       x    x |
|     x       xxxxxx |
|     x              |
----------------------

B 10 3 o
--------------------
|oooooooooooooxxxxx|
|xxxxxxooooooox   x|
|     xoooooooxxxxx|
|     xoooooooooooo|
--------------------
```
# Installation

Uses Python 3: Must have Python downloaded https://www.python.org/downloads/

To install the necessary packages:

pip install pandas
pip install numpy
pip install unittest
pip install numpy.testing

To learn more about how to work with pip: https://packaging.python.org/tutorials/installing-packages/

# To Run

Navigate into script directory
Execute from command-line: python draw.py
Check output folder for drawing and check terminal output for any messages.

# Tests

To run unit tests: python -m unittest tests
To test different pre-made inputs: Get files in /inputs/tests folder
    


