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
    

def chart():
    matrix = np.zeros((10, 2))
    print (matrix)
    for i in range(10):
        matrix[i][0]= input("Enter X! ")
        matrix[i][1]= input("Enter Y! ")
    print (matrix)
    return matrix



def work(n = 10):
    x = np.linspace(0, 10, n)
    #x = np.arange(0, 10, n)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("point num")
    plt.ylabel("sin function")
    plt.title("some chart")
    plt.show()


def main():
    #arr = get_nums()
    
    #parabola(arr[0], arr[1], arr[2])

    chart()


main()