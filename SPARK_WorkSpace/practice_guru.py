# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:36:15 2021

@author: eefhiio
"""

from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize([1,2,3,4,5])

squared_numbers = numbers.map(lambda x: x*x).collect()
print(f"squared_numbers = {squared_numbers} type = {type(squared_numbers)}")


squared_numbers_rdd = numbers.map(lambda x: x*x)
print(f"squared_numbers_rdd Type = {squared_numbers_rdd}")
for number in squared_numbers_rdd.collect():
    print(number)

sc.stop()