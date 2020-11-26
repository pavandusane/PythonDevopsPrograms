#!/usr/bin/env python
# coding:utf-8
"""
Name : flip_coin.py
Author : Pavan Dusane
Time    : 11/23/2020 4:37 PM
Title : Flip Coin and print percentage of Heads and Tails
Desc: Calculate the percentage of flip coin

"""
import random
class flipCoin():

    def calculateFlipPercentage(self,number_of_flip_coin):
        head_count = 0
        tail_count = 0
        temp=number_of_flip_coin
        while number_of_flip_coin>=1:
            no_of_flip=random.randint(0, 1)
            if no_of_flip==0:
                head_count=head_count+1
                number_of_flip_coin=number_of_flip_coin-1
            else:
                tail_count=tail_count+1
                number_of_flip_coin=number_of_flip_coin-1
        return head_count,tail_count,temp

while True:
    try:
        number_of_flip_coin=float(input("Enter the number of times to flip the coin : "))
        if number_of_flip_coin<0:
            print("Please Enter Valid Digit")
            continue
        flipCoin_Object=flipCoin()
        head_count,tail_count,temp=flipCoin_Object.calculateFlipPercentage(number_of_flip_coin)
        print("Percentage of Head Count is : ", (head_count / temp) * 100)
        print("Percentage of Tail Count is : ", (tail_count / temp) * 100)

    except ValueError:
        print("Please Enter Digit Value")
        continue
    except:
        print("Exception Occured")



