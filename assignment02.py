# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


def get_nums():
    a = input("Please enter A: ")
    aint = int(a)
    b = input("Please enter B: ")
    bint = int(b)
    c = input("Please enter C: ")
    cint = int(c)
    return [aint, bint, cint]
    

def parabola(a, b, c):
    x = np.linspace(-50, 50, 1000)    
    y = a*x*x + b*x + c
    plt.plot(x, y)
    plt.xlabel("Xaxis")
    plt.ylabel("Yaxis")
    plt.title("Parabola")
    return [x,y]

def chart():
    matrix = np.zeros((10, 2))
    print (matrix)
    for i in range(10):
        matrix[i][0]= input("Enter X! ")
        matrix[i][1]= input("Enter Y! ")
    print (matrix)
    return matrix


def sum(a, b, c, matrix_points):
    distance_sum = 0
    mistake_sum = 0
    func_points = parabola(a, b, c)
    for i in range(len(func_points[0])):
        distance_sum += np.abs(func_points[1][i])
    for i in range(len(matrix_points[0])):
        mistake_sum += 1-contains(matrix_points[i], func_points)
    return [distance_sum, mistake_sum]
        

def contains(point, parabola):
    for i in range (len(parabola[0])):
        if parabola[0][i] == point[0] and parabola[1][i] == point[1]:
            return True
    return False


def stupid_question(abc):
    best_abc = abc
    matching_points = 0
    const_points = parabola(abc[0], abc[1], abc[2])
    for i in range(50):
        temp = get_nums()
        if (sum(temp[0], temp[1], temp[2], const_points)[1] > matching_points):
            matching_points = sum(temp[0], temp[1], temp[2], const_points)[1]
            best_abc = temp
    return best_abc
            


def main():
    arr = get_nums()  
    parabola(arr[0], arr[1], arr[2])
    chart()
    


main()
