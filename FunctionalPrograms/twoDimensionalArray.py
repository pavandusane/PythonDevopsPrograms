#!/usr/bin/env python
# coding:utf-8
"""
Name : Two_Dimensional_Array.py
Author : Pavan Dusane
Time    : 11/23/2020 6:49 PM
Title : 2D Array
Desc: A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.

"""

class TwoDimensionalArray:
    def __init__(self,no_of_rows,no_of_columns):
        """
                            Initialize the constructor using parameters
        """
        self.no_of_rows=no_of_rows
        self.no_of_columns=no_of_columns

    def calculateMatrix(self):
        """
                define calculateMatrix method to calculate two dimensional matrix
        """
        matrix = []
        for rows in range(self.no_of_rows):
            data = []
            for columns in range(self.no_of_columns):
                data.append(int(input()))
            matrix.append(data)

        for rows in range(self.no_of_rows):
            for columns in range(self.no_of_columns):
                    print(matrix[rows][columns], end="  ")
            print()

        return matrix

try:
    no_of_rows=int(input("Enter number of rows : "))
    no_of_columns=int(input("Enter number of columns : "))
    '''
        take input from user and call the methods using object 
    '''
    two_dimensional_array_object = TwoDimensionalArray(no_of_rows,no_of_columns)
    z=two_dimensional_array_object.calculateMatrix()
    print(z)

except ValueError:
    print("Please Enter Int Value")
except:
    print("Exception Occured")

