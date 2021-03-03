from pyspark import find_spark_home,SparkConf,SparkContext

print("Path-",find_spark_home._find_spark_home())
conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf = conf)

lines = sc.textFile(r"C:\Users\eefhiio\Documents\MyStuff\Hustle\SPARK_Udemy\MovieLens\ml-100k\u.data")
movies = lines.map(lambda x: (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

flipped = movieCounts.map(lambda xy: (xy[1], xy[0]))
sortedMovies = flipped.sortByKey()

results = sortedMovies.collect()

for result in results:
    print(result)
else:
    print("No Results")
