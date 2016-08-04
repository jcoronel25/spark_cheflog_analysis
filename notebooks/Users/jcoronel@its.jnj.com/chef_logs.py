# Databricks notebook source exported at Thu, 4 Aug 2016 20:31:03 UTC
# MAGIC %fs ls /FileStore/tables/pwymmu451470340071320/chef_client-ba119.log

# COMMAND ----------

df1 = sqlContext.read.text("/FileStore/tables/pwymmu451470340071320/chef_client-ba119.log")

# COMMAND ----------

