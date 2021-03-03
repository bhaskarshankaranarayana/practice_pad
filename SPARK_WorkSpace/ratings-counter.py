from pyspark import SparkConf, SparkContext
'''Spark Contest provides fundamentals to create RDD, its the starting point.
Spark Conf allows you to configure and import Spark Context and the script of your code and running it'''
import collections  # importing the collections to store and sort the final results.

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
''' setting up the Spark configuration object.
SparkConf().setMaster(local) makes the local machine/node as master node. setAppName() sets the Application name as "RatingsHistogram"'''
sc = SparkContext(conf = conf)  # using the Spark Configuration obj, we will set up our SparkContext obj.

lines = sc.textFile(r"C:\Users\eefhiio\Documents\MyStuff\Hustle\SPARK_Udemy\MovieLens\ml-100k\u.data")
# print("Type of lines: ", type(lines), "printing Lines:--->", lines.top(15))
''' Creates an RDD by loading the text file data of movie ratings.
it loads the data to RDD line-by-line as a string. 1 row is 1 string.
'''
ratings = lines.map(lambda x: x.split()[2])  # Reads each line and splits it based on whitespace and fetches data at 2nd index in the line string, Adds it to new RDD "ratings". maps function will create new RDD based on each line in lines RDD and keep it syncd, without modifying the lines RDD
result = ratings.countByValue()
'''gives a tuple of how many times each unique values occured. "(uniqueNumber, Count)
 It is as action, hence retunrs plain python object as result'''

sortedResults = collections.OrderedDict(sorted(result.items())) # creates an orderdDict from the result Tuple and sotres it.
for key, value in sortedResults.items():   #loop through the Dict and prints the Key value pairs.
    print("%s %i" % (key, value))
