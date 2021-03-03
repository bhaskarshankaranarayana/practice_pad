from pyspark import SparkConf, SparkContext
import re

def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())


conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("book.txt")
words = input.flatMap(normalizeWords)
wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y)
wordsInSortedCount = wordCounts.sortBy(lambda x: x[1])

result = wordsInSortedCount.collect()

for res in result:
    count = res[1]
    word = res[0].encode('ascii','ignore')
    if word:
        print(str(word) + "\t\t" + str(count))
