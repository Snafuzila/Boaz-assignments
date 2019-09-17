# -*- coding: utf-8 -*-
"""
Made by Boaz.A
Big:    get two matrixes. return the addition of them.
        *note - return matrix with the maximum size, meaning one matrix doesn't
        have to be the same size as the other one, it will create empty space.
    
Small:    get two matrixes. return the addition of them.
          *note - return matrix with the minimum size, meaning both places
          of the matrixes exist, it will ignore some values.
          
"""

import numpy as np


def Big(matrix1, matrix2):    
    width = matrix1.shape[0]
    height = matrix1.shape[1]
    
    if width < matrix2.shape[0]:
        width = matrix2.shape[0]        
    if height < matrix2.shape[1]:
        height = matrix2.shape[1]
        
    big_matrix = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            try:
                big_matrix[i,j] = matrix1[i, j] + matrix2[i, j]
            except:
                pass
    return big_matrix
    

def Small(matrix1, matrix2):    
    width = matrix1.shape[0]
    height = matrix1.shape[1]
    
    if width > matrix2.shape[0]:
        width = matrix2.shape[0]        
    if height > matrix2.shape[1]:
        height = matrix2.shape[1]
        
    small_matrix = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            small_matrix[i,j] = matrix1[i, j] + matrix2[i, j]
    return small_matrix


def main():
    matrix1 = np.array(((0,1),(2,3)))
    matrix2 = np.array(((2,5),(0,6),(1,0)))
    Bmatrix = Big(matrix1, matrix2)
    Smatrix = Small(matrix1, matrix2)
    
    print ("Big matrix")
    print (Bmatrix)

    print ("Small matrix")
    print (Smatrix)
    
    
main()