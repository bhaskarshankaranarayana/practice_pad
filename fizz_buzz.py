# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:51:35 2021

@author: eefhiio
"""
def fizzBuzz():
    for i in range(1,1001):
        display = ""
        if i % 3 == 0:display+="FIZZ"
        if i % 5 == 0:display+="BUZZ"
            
        if display == "":
            print(i)
        else:
            print(display)


fizzBuzz()

        
        