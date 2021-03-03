# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:21:55 2021

@author: eefhiio
"""

import tokenize
import os

from pyspark import SparkContext
from pyspark import SparkConf
from googletrans import Translator

translator = Translator()
sc = SparkContext.getOrCreate()

folder_path = r"C:/Users/eefhiio/OneDrive - Ericsson AB/MELA_CU_LAS-CC_AUTOMATION/code/CC_v10"

def getPyFiles(ext):
    file_list = []
    for file in os.listdir(folder_path):
        if file.endswith(ext):
            file_list.append(file)
    return file_list

def readFileForComments(file_name):
    file_path = folder_path + '/' + file_name
    fileObj = open(file_path, encoding="utf8")
    
    new_file = file_name.split('.')[0]
    
    write_path = folder_path + '/' +new_file +'_COMMENTS.txt'

    with open(write_path, 'a') as fd:
        for toktype, tok, start, end, line in tokenize.generate_tokens(fileObj.readline):
            # we can also use token.tok_name[toktype] instead of 'COMMENT'
            # from the token module 
            if toktype == tokenize.COMMENT:
                # print (tok)
                fd.write(f'\n{tok}')
                
def translateFunction(file_name):
    # Read file into RDD
    file_path = folder_path + '/' + file_name
    lines = sc.textFile(file_path)
    # Call collect() to get all data
    line_list = lines.collect()
    new_file = file_name.split('.')[0]
    write_path = folder_path + '/' +new_file +'_TRANSLATED.txt'
    # print line one by line
    with open(write_path, 'a',encoding="utf8") as fd:
        for line in line_list:
            result = translator.translate(line,dest = 'en')
            fd.write("> > > > # # # # # < < < <\n")
            fd.write(f'Original Text:  {result.origin}\n')
            fd.write(f'Translated Text:  {result.text}\n')
            fd.write("================================================================================================\n")             
                
if __name__ == "__main__":
    # files = getPyFiles(".py")
    # print(f"PY FILES:{files}")
    # for file in files:
    #     readFileForComments(file)
    # new_files = getPyFiles(".txt")
    # print(f"TXT FILES: {new_files}")
    # for new_file in new_files:
    #     translateFunction(new_file)
    translateFunction("CC_Start_COMMENTS.txt")
    sc.stop()
    
        
    
                