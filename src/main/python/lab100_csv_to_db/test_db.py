import findspark
findspark.init()

from pyspark.sql import SparkSession

# set up a Spark Session
spark = (
    SparkSession
    .builder
    .appName("CSV to DB")
    .config("spark.jars", "/home/niccolo/postgresql-42.2.17.jre6.jar")
    .master("local")
    .getOrCreate()
)

df = (
    spark
    .read
    .format("jdbc")  # Specifies the input data source format. We use Java Database Connectivity.
    .option("url", "jdbc:postgresql://localhost:5432/spark_labs")
    # .option("dbtable", "test")  # we created a test table in pgAdmin
    .option("dbtable", "ch02")  # table created with other python script
    # make sure jgp user has access to the table. Create this user with the commands in the README.md.
    .option("user", "jgp")
    .option("password", "Spark<3Java")
    .option("driver", "org.postgresql.Driver")
    .load()
)

print(df.toPandas())
