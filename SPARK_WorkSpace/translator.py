# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:26:53 2021

@author: eefhiio
"""
# # from googletrans import Translator
# from translate import translator as trans

# # translator = Translator()

# py_trans = trans('pt','en',"POPULAR O dict_EXEC COM OS PACOTES QUE SERÃO EXECUTADOS")

# # result = translator.translate("# POPULAR O dict_EXEC COM OS PACOTES QUE SERÃO EXECUTADOS",src='pt',dest='en')

# print(result.text,result.origin)
###################################################################################################################
from pyspark import SparkContext
from pyspark import SparkConf
from googletrans import Translator

translator = Translator()
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.in',
#     ])

# create Spark context with Spark configuration
conf = SparkConf().setAppName("read text file in pyspark")
sc = SparkContext.getOrCreate(conf)

# Read file into RDD
lines = sc.textFile(r"C:/Users/eefhiio/OneDrive - Ericsson AB/MELA_CU_LAS-CC_AUTOMATION/code/try_translate/CC_v10/CC_EXECUTE.py")

# Call collect() to get all data
llist = lines.collect()

# print line one by line
with open(r"C:/Users/eefhiio/OneDrive - Ericsson AB/MELA_CU_LAS-CC_AUTOMATION/code/try_translate/CC_v10/CC_EXECUTE_en.txt", 'a') as fd:
    for line in llist:
        result = translator.translate(line,dest = 'en')    
        fd.write(f'\n{result.text}')
        
    
sc.stop()