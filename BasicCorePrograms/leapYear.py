#!/usr/bin/env python
# coding:utf-8
"""
Name : leap_year.py
Author : Pavan Dusane
Time    : 11/23/2020 5:01 PM
Title : Leap Year
Desc: Check input year is leap year or not

"""

class LeapYear:

    def checkLeapYear(self,input_year1):
        input_year=int(input_year1)
        length_of_year=len(input_year1)
        if length_of_year!=4:
            print("Please Enter Valid Year")
        else:
            if input_year%4==0:
                if input_year%100==0:
                    if input_year%400==0:
                        print("The Given Year is : ",input_year," is leap year")
                    else:
                        print("The Given Year is : ",input_year," is not leap year")
                else:
                    print("The Given Year is : ",input_year," is leap year")
            else:
                print("The Given Year is : ",input_year," is not leap year")


input_year=input("Enter the year : ")
leapYearObject=LeapYear()
leapYearObject.checkLeapYear(input_year)
