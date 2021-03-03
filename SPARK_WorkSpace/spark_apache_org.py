from pyspark.sql import SparkSession

log_file = "C:\spark\README.md"
spark = SparkSession.builder.appName("Simple_App").getOrCreate()
log_data = spark.read.text(log_file).cache()

numb_A = log_data.filter(log_data.value.contains('the')).count()
numb_B = log_data.filter(log_data.value.contains('is')).count()

print(f"Lines with a: {numb_A}, lines with b: {numb_B}")

spark.stop()