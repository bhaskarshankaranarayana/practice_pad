from pyspark import SparkContext,SparkConf

def loadMovieNames():
    movieNames = {}
    with open(r"C:\Users\eefhiio\Documents\MyStuff\Hustle\SPARK_Udemy\MovieLens\ml-100k\u.ITEM") as file:
        for line in file:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

conf = SparkConf().setMaster("local").setAppName("popular-movies-nicer")
sc = SparkContext(conf=conf)
movieNameDict = sc.broadcast(loadMovieNames())

lines = sc.textFile(r"C:\Users\eefhiio\Documents\MyStuff\Hustle\SPARK_Udemy\MovieLens\ml-100k\u.data")
movies = lines.map(lambda x: (int(x.split()[1]),1))
moviesCounts = movies.reduceByKey(lambda x,y:x+y)
movieCountsSorted = moviesCounts.sortBy(lambda x: x[1])

moviesWithName = movieCountsSorted.map(lambda x:(movieNameDict.value[x[0]],x[1]))

result = moviesWithName.collect()

for res in result:
    print (res)
