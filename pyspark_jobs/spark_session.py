from pyspark.sql import SparkSession

class SparkSessionManager:
    _instance = None

    @classmethod
    def get_spark_session(cls):
        if cls._instance == None:
            cls._instance = (
                SparkSession.builder
                .appName('APISenseAI')
                .master('local[*]')
                .getOrCreate()
            )

            cls._instance.sparkContext.setLogLevel("ERROR")

        return cls._instance