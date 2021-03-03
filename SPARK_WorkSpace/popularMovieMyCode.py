from pyspark import SparkContext,SparkConf
import operator
conf = SparkConf().setMaster("local").setAppName("Popular-Movie")
sc = SparkContext(conf=conf)

lines = sc.textFile(r"C:\Users\eefhiio\Documents\MyStuff\Hustle\SPARK_Udemy\MovieLens\ml-100k\u.data")
popularity = lines.map(lambda x:x.split()[1])
movies = popularity.countByValue()
print(max(movies.items(), key=operator.itemgetter(1)))