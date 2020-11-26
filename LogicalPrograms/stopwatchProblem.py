#!/usr/bin/env python
# coding:utf-8
"""
Name : StopwatchProblem.py
Author : Pavan Dusane
Time    : 11/24/2020 8:15 PM
Title : Simulate Stopwatch Program
Desc: Create a program for stopwatch to display elapsed time

"""
import time
class Stopwatch():

    def elapsed_time_display(self,second_time):
        """
            define methods to display elapsed time in time format
        """
        minute_time = second_time // 60
        second_time = second_time % 60
        hours_time = minute_time // 60
        minute_time = minute_time % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours_time), int(minute_time), int(second_time)))


stopwatch_object=Stopwatch()
input("Press Enter to start time : ")
start_time = time.time()
"""
            press enter key to start time and enter key to stop key
"""
input("Press Enter to stop time")
stop_time = time.time()
time_lapsed = stop_time - start_time
"""
            calculate elapsed time using start time and stop time        
"""
stopwatch_object.elapsed_time_display(time_lapsed)
