import os
import sys
import findspark

os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["SPARK_HOME"] = r"C:\spark\spark-3.5.9-bin-hadoop3"

findspark.init()

from pyspark.sql import functions as F

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Aula 02 Spark') \
    .getOrCreate()

dados_vendas = [
    (101, "Eletrônicos", 1500.0, "Concluída"),
    (102, "Vestuário", 200.0, "Concluída"),
    (103, "Eletrônicos", 800.0, "Cancelada"),
    (104, "Eletrônicos", 3000.0, "Concluída"),
    (105, "Vestuário", 150.0, "Concluída")
]

df_vendas = spark.createDataFrame(dados_vendas, ['id', 'tipo', 'valor', 'status'])

df_filtro = df_vendas.filter(
    F.col('status') == 'Concluída'
)

df_faturamento = df_filtro.agg(
    F.sum('valor').alias('faturamento_total')
)

df_faturamento.show()