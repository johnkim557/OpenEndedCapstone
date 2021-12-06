from pyspark.sql import SparkSession

session = SparkSession.builder.master('local').appName('app').getOrCreate()

container = 'capstoneblobstorage'
storage_account_name = 'capstonestoragewayne'
sas_token = 'sp=racw&st=2021-12-03T18:04:44Z&se=2021-12-31T02:04:44Z&spr=https&sv=2020-08-04&sr=c&sig=6DCG%2F9peQGqLMbIzg7GL3In8LeBSd9Tiv61cz7OdyGk%3D'

session.conf.set(f"fs.azure.sas.{storage_account_name}.azcopyblobstorage.blob.core.windows.net",sas_token)


key = 'lbIPh+FPE4wXV6RcLcDZwqSy22U/ZymZeiAVOh/lVp0nmEIZvvGwhiDTK6jp7IJ5sKq5j5Ak7L6YbXWJDDy2Og=='

dbutils.fs.mount(
  source = f"wasbs://{container}@{storage_account_name}.blob.core.windows.net",
  mount_point = "/mnt/azureStorage",
  extra_configs = {f"fs.azure.account.key.capstonestoragewayne.blob.core.windows.net": key}key = 'lbIPh+FPE4wXV6RcLcDZwqSy22U/ZymZeiAVOh/lVp0nmEIZvvGwhiDTK6jp7IJ5sKq5j5Ak7L6YbXWJDDy2Og=='

dbutils.fs.mount(
  source = f"wasbs://{container}@{storage_account_name}.blob.core.windows.net",
  mount_point = "/mnt/azureStorage",
  extra_configs = {f"fs.azure.account.key.capstonestoragewayne.blob.core.windows.net": key}

%fs ls "dbfs:/mnt/azureStorage"

df = spark.read.option("header",True) \
     .csv("dbfs:/mnt/azureStorage/restaurants-database.csv")

df.filter(df2.STATE =='NJ').show()

df.filter(df2.STATE == 'NJ').count()