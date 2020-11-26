#!/usr/bin/env python
# coding:utf-8
"""
Name : harmonic_number.py
Author : Pavan Dusane
Time    : 11/23/2020 5:04 PM
Title : Harmonic Number
Desc: Print the total harmonic sum of given number

"""
def harmonicNumber():

    res=0
    number=int(input("Enter the number : "))
    for index in range(1,number):
        res1=(1/index)
        res=res+res1
        index=index+1
    print(res)

harmonicNumber()