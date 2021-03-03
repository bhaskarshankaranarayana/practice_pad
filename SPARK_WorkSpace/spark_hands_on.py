# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:05:18 2021

@author: eefhiio
"""
from pyspark import SparkContext

sc = SparkContext.getOrCreate()

#reads lines of text file to rdd
lines = sc.textFile(r"C:\Users\eefhiio\OneDrive - Ericsson AB\MELA_CU_LAS-CC_AUTOMATION\docs\Questions.txt")
#finds the length of each lines or char in each lines
lines_length = lines.map(lambda l: len(l))
#calculates the total chars or complete length of each lines in file
total_length = lines_length.reduce(lambda a,b:a+b)


#SAVES IN CACHE MEMORY FOR QUICK ACCESS FOR LATER PURPOSE
# total_length.persist()

pairs = lines.map(lambda s:(s,1))
counts = pairs.reduceByKey(lambda a,b:a+b)

data = counts.collect()

sorted_data = counts.sortByKey().collect()


sc.stop()