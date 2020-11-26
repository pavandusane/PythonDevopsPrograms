#!/usr/bin/env python
# coding:utf-8
"""
Name : Triplet_Zero.py
Author : Pavan Dusane
Time    : 11/23/2020 6:50 PM
Title : Sum of three Integer adds to ZERO
Desc: A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.

"""
from array import *

class tripletZero():
    def __init__(self,size):
        """
                            Initialize the constructor using parameters
        """
        self.size=size

    def calculateTriplet(self):
        """
            define calculateTriplet method to calculate the triplet of number where there sum is zero
        """
        arr = array('i', [])
        for i in range(size):
            print("Enter the numbers : ")
            numbers = int(input())
            arr.append(int(numbers))

        print("You have entered : ")
        print(arr)
        x = len(arr)
        for i in range(x):
            fno = arr[i]
            i = i + 1
            for j in range(x):
                sno = arr[j]
                j = j + 1
                for k in range(x):
                    tno = arr[k]
                    k = k + 1
                    sum = fno + sno + tno
                    if sum == 0:
                        print(fno,sno,tno)
try:
    size=int(input("Enter the no of element you want add : "))
    tripletZero_obj=tripletZero(size)
    fno,sno,tno=tripletZero_obj.calculateTriplet()
    #print("The triplet of above numbers are : ",fno,sno,tno)
except ValueError:
    print("Please Enter Int Value : ")
except:
    print("No triplet found ")


