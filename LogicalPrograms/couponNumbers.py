#!/usr/bin/env python
# coding:utf-8
"""
Name : CouponNumbers.py
Author : Pavan Dusane
Time    : 11/24/2020 4:34 PM
Title : Coupon Numbers
Desc: Desc -> Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? This program simulates this random process.
I/P -> N Distinct Coupon Number
Logic -> repeatedly choose a random number and check whether it's a new one.
O/P -> total random number needed to have all distinct numbers.
Functions => Write Class Static Functions to generate random number and to process distinct coupons.

"""
import random
class CouponNumber():

    def __init__(self,take_number):
        """
            constructor initialize using parameter
        """
        self.take_number=take_number

    def calculateDistinctNumber(self):
        """
            define method to calculate distinct coupon number
        """
        distict_number=[]
        while len(distict_number)<self.take_number:
            rand = random.randrange(0, self.take_number)
            if  rand not in distict_number:
                distict_number.append(rand)
            else:
                pass
        return distict_number

while True:
    try:
        take_number=int(input("Enter the distinct number : "))
        if take_number<0:
            print("Please Enter Positive Digits")
            continue
            """
                taking input from user
            """
        coupon_number_object=CouponNumber(take_number)
        total_random_number=coupon_number_object.calculateDistinctNumber()
        print("Total Distinct Coupon Number : ",total_random_number)
    except ValueError:
        print("Please Enter Digit Value")
    except:
        print("Exception Occured")

