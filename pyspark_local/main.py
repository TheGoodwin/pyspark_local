
# Create SparkSession from builder
import pyspark
from pyspark.sql import SparkSession

spark : SparkSession = SparkSession.builder.master("local[*]") \
                    .appName('pyspark_local') \
                    .getOrCreate()

births = (
    spark.read.format("csv")
    .option("header", "true")
    .load("data/inputs/births/*.csv")
)

births.show(10)

print("Hello world !")
