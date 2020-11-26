#!/usr/bin/env python
# coding:utf-8
"""
Name : Euclidean Distance.py
Author : Pavan Dusane
Time    : 11/23/2020 6:54 PM
Title : Calculate Euclidean Distance
Desc: Takes two integer command-line arguments x and y and prints the Euclidean distance.
"""
import math as m

class EuclideanDistance():

    def calculate_euclidean_distance(self,coeficient_of_x1,coeficient_of_y1,coeficient_of_z1,coeficient_of_x2,coeficient_of_y2,coeficient_of_z2):
        """
                        define method and calculate euclidean distance of given inputs

        """
        calculate_delta1_for_exp1=coeficient_of_x2-coeficient_of_x1
        calculate_delta2_for_exp2=coeficient_of_y2-coeficient_of_y1
        calculate_delta3_for_exp3=coeficient_of_z2-coeficient_of_z1

        square_of_delta1=m.pow(calculate_delta1_for_exp1,2)
        square_of_delta2=m.pow(calculate_delta2_for_exp2,2)
        square_of_delta3=m.pow(calculate_delta3_for_exp3,2)

        result_of_delta1=m.sqrt(square_of_delta1)
        result_of_delta2=m.sqrt(square_of_delta2)
        result_of_delta3=m.sqrt(square_of_delta3)

        final_result_of_expre=result_of_delta1+result_of_delta2+result_of_delta3

        return final_result_of_expre
while True:
    try:
        coeficient_of_x1,coeficient_of_y1,coeficient_of_z1 = map(int, input("Enter the value of x1,y1,z1").split())
        coeficient_of_x2,coeficient_of_y2,coeficient_of_z2 = map(int, input("Enter the value of x2,y2,z2").split())
        EuclideanDistance_object=EuclideanDistance()
        """
                        take input from user

        """
        EuclideanDistance=EuclideanDistance_object.calculate_euclidean_distance(coeficient_of_x1,coeficient_of_y1,coeficient_of_z1,coeficient_of_x2,coeficient_of_y2,coeficient_of_z2)
        print("Euclidean Distance of Given Numbers is : ",EuclideanDistance)
    except ValueError:
        print("Please Enter Digit Value")
        continue
    except:
        print("Exception Occured")

