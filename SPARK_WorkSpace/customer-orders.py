from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sc = SparkContext(conf= conf)

def CustomerData(data):
    fields = data.split(",")
    custId = int(fields[0])
    amountSpent = float(fields[2])
    return custId, amountSpent

lines = sc.textFile("customer-orders.csv")
parsedData = lines.map(CustomerData)
totalAmtSpentByCustomer = parsedData.reduceByKey(lambda x,y: (x + y))
amtSpentInOrder = totalAmtSpentByCustomer.sortBy(lambda x: x[1])
result = amtSpentInOrder.collect()

for res in result:
    print(res)
    
    
sc.stop()    