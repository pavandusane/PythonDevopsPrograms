#!/usr/bin/env python
# coding:utf-8
"""
Name : power_of_two.py
Author : Pavan Dusane
Time    : 11/23/2020 5:03 PM
Title : Power of 2
Desc: Take number from user and print number of power of 2 till reached to given number

"""
import array
class PowerNumber:
    def calculatePowerofTwo(self,user_input):

        index=1
        for index in range(user_input):
            if index<=user_input:
                power_result=pow(2,index)
                if power_result<=user_input:
                    print(power_result)
                    index=index+1
                else:
                    break
            else:
                break

while True:
    try:
        user_input=int(input("Enter the number  : "))
        if user_input<0:
            print("Please Enter Valid Digit Value")
            continue
        power_number_object=PowerNumber()
        power_number_object.calculatePowerofTwo(user_input)
    except ValueError:
        print("Please Enter Digit Value")
        pass
    except:
        print("Exception Occured")
