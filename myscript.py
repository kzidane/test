from pyspark.dbutils import DBUtils

dbutils = DBUtils(spark)

dbutils.jobs.taskValues.set("myval", 42)
