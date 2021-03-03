from pyspark import SparkConf, SparkContext
import re

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("book.txt")
words = input.flatMap(lambda x: re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\:"|<,./<>?]',x))
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + " " + str(count))
