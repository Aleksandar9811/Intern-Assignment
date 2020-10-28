# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:47:32 2020


A function which finds the neighbours of the provided 'position' as a tuple and returns a list
of tuples, the neighbours
"""
#finds the neighbours as tuples of the current position ' position'-as a tuple in  the matrix 'matrix'-2d list
import numpy as np
import sys
def find_neighbours(matrix,position):
    dimensions=np.asarray(matrix).shape
    dimensions=list(dimensions)
    neighbours=[]
    dimensions[0]=dimensions[0]-1
    dimensions[1]=dimensions[1]-1
  
    
    if position[0]!=0:
        if position[1]!=0:
            if position[0]!=dimensions[0]:
                if position[1]!=dimensions[1]:
                    #has four neighbours
                    neighbours=[(position[0]-1,position[1]),
                                (position[0],position[1]-1),(position[0]+1,position[1]),(position[0],position[1]+1)]
                    #has 3 neighbours
                elif position[1]==dimensions[1]:
                    neighbours=[(position[0]-1,position[1]),
                                (position[0],position[1]-1),(position[0]+1,position[1])]
                #has 3 neighbours
            elif position[0]==dimensions[0]:
                #if it is the right-bottom corner
                if position[1]==dimensions[1]:
                    neighbours=[(position[0]-1,position[1]),
                                (position[0],position[1]-1)]
                    #if it is just on bottom line
                else:
                    neighbours=[(position[0]-1,position[1]),
                                (position[0],position[1]-1),(position[0],position[1]+1)]
            
                
        elif position[1]==0:
            #it is in bottom-left corner
            if position[0]==dimensions[0]:
                neighbours=[(position[0]-1,position[1]),
                                (position[0],position[1]+1)]
           
            else:
                #it is just on left line off corners
                neighbours=[(position[0]-1,position[1]),
                                (position[0]+1,position[1]),(position[0],position[1]+1)]
    elif position[0]==0:
        #it is in top left corner
        if position[1]==0:
            neighbours=[(position[0]+1,position[1]),(position[0],position[1]+1)]
        elif position[1]==dimensions[1]:
            #it is in top right corner
            neighbours=[(position[0],position[1]-1),
                                (position[0]+1,position[1])]
        else:
            #it is just on top border line off corners
            neighbours=[(position[0],position[1]-1),(position[0]+1,position[1]),(position[0],position[1]+1)]
      
              
    return neighbours
    

#visited_positions:list of tuples
#current_position:tuple
#returns list of the neighbours positions which are not visited yet
def available_adjacent_positions(matrix,visited_positions,current_position,symbol='R'):
    neighbour_positions=find_neighbours(matrix,current_position)
    a=[]
    for t in neighbour_positions:
        if t in visited_positions:
            neighbour_positions.remove(t)
  
    for d in neighbour_positions:
        if matrix[d[0]][d[1]]==symbol:
            a.append('Yes')
        else:
            a.append('No')
            
    
    if  a.count('Yes')>=1:
        for u in range(len(a)):
            if a[u]=='Yes'and neighbour_positions[u] not in visited_positions:
                current_position=neighbour_positions[u]
                visited_positions.append(neighbour_positions[u])
                
    else:
        current_position='None of the available,not yet visited, positions contains the sign {}'.format(symbol)
        
    
    
    return current_position 



#marks the positions where the symbol appears in the matrix, the others are left as ' ' 

def symbol_positions(matrix,all_positions,symbol='R'):
    
    k=[]
    visited_pos=[]
    for i,j in all_positions:
        l=[]
        if (i,j) not in visited_pos:
            
            if matrix[i][j]==symbol: 
                
                visited_pos.append((i,j))
                l.append((i,j))
        else:
            all_positions.remove((i,j))
            symbol_positions(matrix,all_positions,symbol='R')
        k.append(l)  
    
    dimensions=np.asarray(matrix).shape
    
    
    m=[]  
    for h in range(len(k)):
        if k[h]!=[]:
            for p in range(len(k[h])):
                  m.append(k[h][p])
        elif k[h]==[]:
            m.append(' ')
    f=[]
    for i in range(dimensions[0]):
        a=[]
        for o in range(i*dimensions[1],(i+1)*dimensions[1]):
            a.append(m[o])
        f.append(a)
    return f    
            
def counting(matrix,visited_positions,all_positions,symbol):
    #find where the symbol is located
    p=symbol_positions(matrix,all_positions,symbol)

    for j in p:
        for y in range(len(j)):
            if j[y] in visited_positions:
                j[y]=' '
    m=[]    
    for i in p:
        for h in range(len(i)):
            if i[h]!=' ':
                if i[h] not in visited_positions:
                    visited_positions.append(i[h])
                    #all_positions.remove(i[h])
                    s=find_neighbours(matrix,i[h])
                    for k in s:
                        
                        if matrix[k[0]][k[1]]==symbol and k not in visited_positions: 
                            visited_positions.append(k)
                           
                        
                            counting(matrix,visited_positions,all_positions,symbol)
                            
                        else:
                            
                            continue
                        
                else:
                    break
            m.append(len(visited_positions))            
                   
    return max(m)




        
        
        
        
        
        
    
    
    
    
    
    
