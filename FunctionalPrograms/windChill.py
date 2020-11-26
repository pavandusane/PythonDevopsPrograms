#!/usr/bin/env python
# coding:utf-8
"""
Name : WindChill.py
Author : Pavan Dusane
Time    : 11/23/2020 10:31 PM
Title :  WindChill Problem
Desc: Write a program WindChill.java that takes two double command-line arguments t and v and prints the wind chill.

"""

class windchill:
    def __init__(self,value_of_temperature,value_of_speed):
        """
            Initialize constructor with parameters
        """
        self.value_of_temperature=value_of_temperature
        self.value_of_speed=value_of_speed

    def calculate(self):
        """
            define methods for calculate equation
        """
        weather_service=35.74+0.6215*self.value_of_temperature+(0.4275*self.value_of_temperature-35.75)*pow(self.value_of_speed,0.16)
        #print(weather_service)
        return weather_service

while True:
    try:
        value_of_temperature=int(input("Enter the temperature  (not more than 50) : "))
        if value_of_temperature<0 or value_of_temperature>50:
            print("Please Enter Valid Digit")
            continue
        value_of_speed=int(input("Enter the speed (not more than 120 and less than 3) : "))
        if value_of_speed<3 or value_of_speed>120:
            print("Please Enter Valid Digit")
            continue
        windchill_obj=windchill(value_of_temperature,value_of_speed)
        national_weather_service=windchill_obj.calculate()
        '''
            take input from user and call the methods using object 
        '''
        if national_weather_service==None:
            break
        print("National Weather Service : ",national_weather_service)
    except ValueError:
        print("Please Enter Digit Value")
    except:
        print("Exception Occured")