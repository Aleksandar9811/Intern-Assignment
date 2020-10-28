Two files:
intern.py:
- the main program that calculates the longest adjacent sequence of symbols
that must be chosen from R/G/B;
-the dimensions must be inputted with a single blank space
-the matrix elements must also be inputted also with a single blank space
between every symbol
-if the last two conditions are not met an error will occur
-this program contains error messages for wrongly inputted symbols,for
a matrix that does not correspond to the inputted dimensions
-an error will occur in the situation when a blank space is typed either
after the last symbol on a row or before the first one


intern_helper.py:

function find-neighbours(matrix,position):
finds the positions which are adjacent to the inputted 'position'
-returns a list of tuples- the neighbours' coordinates in the matrix

function symbol_positions(matrix,all_positions,symbol):
-this finds the coordinates in the matrix as tuples where the element symbol 
occurs and the elements with other symbols are set to be empty strings ' '

function counting(matrix,visited_positions,all_positions,symbol):
-the actual function that counts the length of adjacent elements path