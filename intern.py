# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from  intern_helper import available_adjacent_positions,symbol_positions,find_neighbours,counting

dimensions=input("Enter dimensions(rows and columns): ")
    
dimensions=dimensions.split(' ')

dimensions_as_int=[]
for i in dimensions:
    dimensions_as_int.append(int(i))
#dimensions_as_int is now a list with two integers, 1st one is no rows, 2nd is no cols
#make check whether the inputted matrix strings are corresponding to the inputted dimension

print('Enter your matrix of colours with upper-case letters(R/G/B):')
rows_as_strings=[]
for j in range(dimensions_as_int[0]):   #len(dimensions_as_int[0])
    p=input('>')
    rows_as_strings.append(p)
#here rows_as_strings is a list with elements strings, each element is row from the inputted matrix

#create check-tests for correctly inputted matrix
current_row=0
for i in rows_as_strings:
    i=i.split(' ')
    if len(i)!=dimensions_as_int[1]:
        print('Incorrect number of  elements on a row {}'.format(current_row))
        sys.exit()
    for s in i:
        if s not in ['R','G','B']:
            print('Incorrect letter for colour on row {}'.format(current_row))
            sys.exit()
    current_row+=1
#now begin the actual search for longest adjacent sequence

#remove the whitespace b\w the  letters on each row
for u in range(len(rows_as_strings)):
    rows_as_strings[u]=rows_as_strings[u].split(' ')




visited_positions=[]
all_positions=[]
for u in range(dimensions_as_int[0]):
    for t in range(dimensions_as_int[1]):
        all_positions.append((u,t))
counter=0

  
b=[]
for symbol in ['R','B','G']:
    
    b.append(counting(rows_as_strings,visited_positions,all_positions,symbol))          
    visited_positions=[]

print(max(b))            
            
            
       









