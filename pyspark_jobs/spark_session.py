from pyspark.sql import SparkSession
import os
import sys

class SparkSessionManager:
    _instance = None

    @classmethod
    def get_spark_session(cls):
        os.environ["PYSPARK_PYTHON"] = sys.executable
        os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
        if cls._instance == None:
            cls._instance = (
                SparkSession.builder
                .appName('APISenseAI')
                .master('local[*]')
                .getOrCreate()
            )

            cls._instance.sparkContext.setLogLevel("ERROR")

        return cls._instance