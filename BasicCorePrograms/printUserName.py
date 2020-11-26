#!/usr/bin/env python
# coding:utf-8
"""
Name : print_user_name.py
Author : Pavan Dusane
Time    : 11/23/2020 3:06 PM
Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
Desc: Take input from user and print greeting with user name
"""

class UserName:
    def printUserName(self,user_name):
        length_of_user_name=len(user_name)
        if length_of_user_name>3:
            return user_name
        else:
            print("Ufff your name should be more than 3 character")

while True:
    try:
        user_name=input("Enter your name : ")
        user_name_object=UserName()
        result_of_user_name=user_name_object.printUserName(user_name)
        print("Hello "+result_of_user_name+",How are you")
        print("Thank You!!!!")
    except NameError:
        print("Please Enter Valid User Name")
        continue
    except:
        print("Exception Occured")
