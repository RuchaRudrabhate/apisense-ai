from pyspark.sql.functions import (
    col, count, avg, max, min, round, when, desc
)

class AggregationEngine:

    def __init__(self, dataframe):
        self.df = dataframe

    # 1. Total Requests per service 

    def total_request_per_service(self):
        print("\n------ 1. Total Requests per service ------\n")
        self.df.groupBy("service") \
        .count() \
        .orderBy(desc("count")) \
        .show(truncate = False)

    # 2. Status Code Distribution
    def status_code_distribution(self):
        print("\n------ 2. Status Code Distribution ------\n")
        self.df.groupBy("status_code") \
        .count() \
        .orderBy("status_code") \
        .show(truncate = False)

    # 3. Service-wise Status Code Distribution
    def service_wise_status_distribution(self):
        print("\n------  3. Service-wise Status Code Distribution ------\n")
        self.df.groupBy("service","status_code") \
        .count() \
        .orderBy("service", "status_code") \
        .show(truncate = False)

    # 4. Average Latency Per Service
    def latency_statistics(self):
        print("\n------  4. Average Latency Per Service ------\n")
        self.df.groupBy("service") \
            .agg(
                round(avg("latency_ms"), 2).alias("avg_latency"),
                max("latency_ms").alias("max_latency"),
                min("latency_ms").alias("min_latency")
            ) \
            .orderBy(desc("avg_latency")) \
            .show(truncate=False)
        
    # 5. Error Count Per Service
    def error_count_per_service(self):
        print("\n------ 5. Error Count Per Service ------\n")

        self.df.filter(col("status_code") >= 400) \
        .groupBy('service') \
        .count() \
        .orderBy(desc("count")) \
        .show(truncate = False)

    # 6. Error Rate Per Service
    def error_rate_per_service(self):
        print("\n------ 6. Error Rate Per Service ------\n")

        total_request = self.df.groupBy("service") \
        .agg(count("*").alias("total_request"))

        error_requests = self.df.filter(col("status_code") >= 400) \
            .groupBy("service") \
            .agg(count("*").alias("error_requests"))

        result = total_request.join(
            error_requests, on = "service", how = 'left'
        ).fillna(0)

        result = result.withColumn(
            "error_rate(%)", 
            round((col('error_requests') / col('total_request')) *100, 2)
        )

        result.orderBy(desc('error_rate(%)')).show(truncate = False)

    # 7. Success vs Failure
    def success_failure_summary(self):
        print("\n------ 7. Success vs Failure ------\n")

        self.df.withColumn(
            "request_type",
            when(col("status_code") < 400, "SUCCESS")
            .otherwise("FAILED")
        ) \
        .groupBy("request_type") \
        .count() \
        .show()

    # 8. Most Frequent Error Messages
    def most_common_errors(self):

        print("\n------ 8. Most Common Error Messages ------\n")

        self.df.filter(col("error_message") != "") \
            .groupBy("error_message") \
            .count() \
            .orderBy(desc("count")) \
            .show(truncate=False)
        
     # 9. Severity Distribution
    def severity_distribution(self):

        print("\n------ 9. Severity Distribution ------\n")

        self.df.groupBy("severity") \
            .count() \
            .orderBy(desc("count")) \
            .show()






