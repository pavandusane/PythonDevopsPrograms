#!/usr/bin/env python
# coding:utf-8
"""
Name : Factors.py
Author : Pavan Dusane
Time    : 11/23/2020 6:27 PM
Title : Factors.py
Desc: Calculate Factorization of Number

"""

class Factorization:
    def calculatePrimeFactorization(self,input_number):
        first_check_number = 1
        while (first_check_number <= input_number):
            count = 0
            if (input_number % first_check_number == 0):
                second_check_number = 1
                while (second_check_number <= first_check_number):
                    if (first_check_number % second_check_number == 0):
                        count = count + 1
                    second_check_number = second_check_number + 1

                if (count == 2):
                    print(" %d is a Prime Factor of a Given Number %d" % (first_check_number, input_number))
            first_check_number = first_check_number + 1

while True:
    try:
        input_number = int(input(" Please Enter any Number: "))
        if input_number<0:
            print("Please Enter Valid Digit")
            continue
        factorization_object=Factorization()
        factorization_object.calculatePrimeFactorization(input_number)
    except ValueError:
        print("Please Enter Digit Value")
        continue
    except:
        print("Exception Occured")