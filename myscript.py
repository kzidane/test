from pyspark.dbutils import DBUtils

dbutils = DBUtils(spark)

dbutils.jobs.taskValues.set('foo', 42)
print(dbutils.jobs.taskValues.get('mytask', 'foo'))
