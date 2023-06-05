# Databricks notebook source
dbutils.widgets.text("Input", "Notebook2")

# COMMAND ----------

notebook = dbutils.widgets.get("Input")

# COMMAND ----------

print("Hello notebook1")

# COMMAND ----------

dbutils.notebook.run(notebook, 60)
