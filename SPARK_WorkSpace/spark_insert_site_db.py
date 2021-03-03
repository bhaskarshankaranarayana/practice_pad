from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import findspark
findspark.init()

# Create spark configuration object
conf = SparkConf().setMaster("local").setAppName("Insert_site_DB")
sc=SparkContext(conf = conf)
conf.setMaster("local").setAppName("Insert Site DB")

# Create spark context and sparksession
# sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)

# read csv file in a dataframe
df = sc.read.csv(path="C:\\Users\eefhiio\Desktop\insert_site_db_hp.csv", header=True, sep=",")

# set variable to be used to connect the database
database = "MVPAT_MASTERDB_NSN_UPE_4G"
table = "MVPAT_CELL_DB_HP"
user = "eefhiio"
password = "eefhiio@123"

# write the dataframe into a sql table
df.write.mode("overwrite") \
    .format("jdbc") \
    .option("url", f"jdbc:sqlserver:10.174.134.74;databaseName={database};") \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .save()