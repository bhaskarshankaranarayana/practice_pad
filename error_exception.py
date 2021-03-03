# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:17:11 2020

@author: eefhiio
"""
def error_try():
        
    try:
        f = open('simple.txt','r')
        f.write("Adding few string to the simple text file!!")
        print('SUCCESS!!!')
    except IOError as e:
        print(f"READ or WRITE Error ,, {e}")
        
    finally:
        
        f.close()
        print("Files closed!")