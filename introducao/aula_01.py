import os
import sys

os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["SPARK_HOME"] = r"C:\spark\spark-3.5.9-bin-hadoop3"

import findspark
findspark.init()

from pyspark.sql import SparkSession # importando o Spark

# Comando inicial para startar o Spark
# O builder é o construtor da sessão. Ele serve para você configurar o Spark antes de ligá-lo (dizer quanta memória ele pode usar, o nome da aplicação, etc.).
spark = SparkSession.builder \
    .appName('Iniciando Spark') \
    .getOrCreate()
# .getOrCreate() é o comando que diz: "Verifique se já existe uma sessão do Spark rodando nesta máquina. Se não existir, crie uma nova; se já existir, utilize a mesma".

# Simulando tabela
dados = [
    (1, "Ana", "São Paulo"),
    (2, "Carlos", "Rio de Janeiro"),
    (3, "Beatriz", "São Paulo")
]

# Criando o DataFrame manualmente
df_spark = spark.createDataFrame(dados, ['id_pedido','cliente', 'cidade'])

# Na vida real é mais ou menos assim
# df_spark = spark.read.csv("s3a://meu-bucket/dados.csv", header=True, inferSchema=True)

# Transformação, aqui o Spark apenas anota(Lazy Evaluation)
df_filtrado = df_spark.filter(df_spark['cidade'] == 'São Paulo')

# Para chamar uma ação você precisa utilizar o .count(), .write() ou o .show(), se não ela ira continuar em Lazy
df_filtrado.show()