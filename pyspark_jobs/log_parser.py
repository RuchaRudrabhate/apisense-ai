from pyspark.sql.functions import (col, to_timestamp)
from spark_session import SparkSessionManager
from aggregation import AggregationEngine

class LogParser:
    def __init__(self):
        self.spark = SparkSessionManager.get_spark_session()

    def read_logs(self, path):
        df = self.spark.read.json(path)
        return df
    
    def parse_timestamps(self, df):
        parsed_df = df.withColumn("timestamp", to_timestamp(col("timestamp")))
        return parsed_df
    
    def show_schema(self, df,limit = 10):
        print("log_parser.show_schema()->Dataframe Schema")
        df.printSchema()
        print("log_parser.show_schema()-> First 10 rows")
        df.show(limit, truncate=False)
        print("\n\n")

    def show_total_log_count(self, df):
        print("log_parser.show_total_log_count()-> Total Logs Count:")
        print(df.count())
        print("\n\n")

    def show_status_distribution(self, df):
        print("log_parser.show_status_distribution()-> Show Status Code Distribution")
        df.groupBy("status_code")\
        .count() \
        .orderBy("status_code") \
        .show()

    def show_service_distribution(self, df):
        print("log_parser.show_service_distribution()-> Show Service Distribution")
        df.groupBy("service") \
        .count() \
        .orderBy("service") \
        .show()

if __name__ == "__main__":
    parser = LogParser()
    logs_df = parser.read_logs("datasets/logs.json")

    parser.show_schema(logs_df)

    parsed_logs_df = parser.parse_timestamps(logs_df)

    parser.show_total_log_count(parsed_logs_df)

    parser.show_status_distribution(parsed_logs_df)

    parser.show_service_distribution(parsed_logs_df)

    aggregation_engine =AggregationEngine(parsed_logs_df)

    aggregation_engine.total_request_per_service()
    aggregation_engine.status_code_distribution()
    aggregation_engine.service_wise_status_distribution()
    aggregation_engine.latency_statistics()
    aggregation_engine.error_count_per_service()
    aggregation_engine.error_rate_per_service()
    aggregation_engine.success_failure_summary()
    aggregation_engine.most_common_errors()
    aggregation_engine.severity_distribution()

