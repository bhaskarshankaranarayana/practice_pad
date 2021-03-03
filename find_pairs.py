# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:45:16 2021

@author: eefhiio
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # print(set(ar))
    # total = 0
    # for ele in set(ar):
    #     count = ar.count(ele)//2
    #     print("COUNT",count)
    #     total = total + count
    # print(total)
    return sum([ar.count(i)//2 for i in set(ar)])

    

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    
