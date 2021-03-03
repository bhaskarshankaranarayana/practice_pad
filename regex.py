# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:30:46 2020

@author: eefhiio
"""

import re
from error_exception import error_try

pattern = ['hello','Good Morning']

text_msg = 'Hey Jose, Good Morning'

for pat in pattern:
    print(f"Searching for {pat}")
    
    if re.search(pat,text_msg):
        print(f"{pat} Its a match!")
    else:
        print(f"{pat} is not a match")
        

match = re.search('Good',text_msg)
print(f'Type of Match : {type(match)}')
print(f'Match : {match}')
print(f'SPAN : {match.span()}')
print(f'ENDING index : {match.span()[1]}')

print(f'starting index {match.start()}') # start method

print(re.split(',',text_msg))

print(re.findall('o',text_msg)) #findall method
print(len(re.findall('o',text_msg)))


def multi_re_findall(patterns,phrase):
    for patt in patterns:
        print(f"searching for {patt}")
        print(re.findall(patt,phrase),"\n")
        
test_str = 'sddddd........sdds....ssddsd.sd...dsdsdsdsds.......ssddsdsdsddd.......sddddddssddsdsdsdsds'

test_pat = ['sd*'] #0 or more occurances of d
multi_re_findall(test_pat,test_str)

test_pat = ['sd+'] #1 or more occurances of d
multi_re_findall(test_pat,test_str)

test_pat = ['sd?'] #0 or more occurances of d
multi_re_findall(test_pat,test_str)


test_pat = ['sd{2}'] #specific count occurances of d
multi_re_findall(test_pat,test_str)

test_pat = ['sd{2,3}'] #specific count 2 or 3 occurances of d
multi_re_findall(test_pat,test_str)

test_pat = ['s[sd]+'] #1 or more occurance of s or d after s
multi_re_findall(test_pat,test_str)



new_test_str = 'This stirng cont@ins lot of Punctuation! please try to Ignore them..'

test_pat_1 = ['[^!@.?]+']#ignore 1 or more occurance of all the chars after ^ more like a multiple split
multi_re_findall(test_pat_1,new_test_str)

test_pat_1 = ['[a-z]+']#lower case
multi_re_findall(test_pat_1,new_test_str)

test_pat_1 = ['[A-Z]+']#lower case
multi_re_findall(test_pat_1,new_test_str)


new_test_str_1 = 'This stirng cont@ins lot of numbers 1234567890 and symbols like !@#$%^&*'

test_pat_1 = [r'\d+']#search for digits \d
multi_re_findall(test_pat_1,new_test_str_1)   


test_pat_1 = [r'\D+']#search for  non digits \D
multi_re_findall(test_pat_1,new_test_str_1)   


test_pat_1 = [r'\s+']#search for  white spaces \s
multi_re_findall(test_pat_1,new_test_str_1)   

test_pat_1 = [r'\S+']#search for  non white spaces \S
multi_re_findall(test_pat_1,new_test_str_1) 

test_pat_1 = [r'\w+']#search for alpha-numeric  \w
multi_re_findall(test_pat_1,new_test_str_1) 

test_pat_1 = [r'\W+']#search for non alpha-numeric  \W including white spaces
multi_re_findall(test_pat_1,new_test_str_1) 

error_try()