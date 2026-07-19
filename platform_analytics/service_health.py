"""
Determine how healthy every service is.
example:
payment-api
Availability : 97%
Average Latency : 280 ms
Error Rate : 3%
Health : HEALTHY

For every service, calculate:

- Total Requests
- Failed Requests
- Error Rate (%)
- Average Latency
- Maximum Latency
- Availability
- Health Status
- Health Score
"""
from pyspark.sql.functions import (
    col,
    count,
    avg,
    max as spark_max,
    round as spark_round,
    when
)

from platform_analytics.base_analyzer import BaseAnalyzer
from platform_analytics.constants import (
    DEFAULT_THRESHOLDS,
    SERVICE_THRESHOLDS
)

class ServiceHealthAnalyzer(BaseAnalyzer):

    def __init__(self, dataframe):
        super().__init__(dataframe)

    def calculate_service_health(self):
        """
        Returns health statistics for every service.
        """
        self.validate_dataframe()

        # Total requests per service
        total_requests = self.df.groupBy("service") \
        .agg(
            count("*").alias("total_requests")
        )

        # Failed requests per service
        failed_requests = self.df.filter(
            col("status_code") >=400
        ).groupBy("service") \
        .agg(
            count("*").alias("failed_requests")
        )

        # Average latency
        latency = self.df.groupBy("service") \
            .agg(
                spark_round(avg("latency_ms"), 2).alias("avg_latency_ms"),
                spark_max("latency_ms").alias("max_latency_ms")
            )
        
        # Merge everything

        result = total_requests \
        .join(failed_requests, "service", "left") \
        .join(latency, "service")

        result = result.fillna(0)

        # Error Rate
        result = result.withColumn(
            "error_rate",
            spark_round(
                (col("failed_requests") / col("total_requests")) *100, 2
            )
        )

        # Availability

        result = result.withColumn(
            "availability",
            spark_round(100 - col("error_rate") , 2)
        )

        return result
    
    def assign_health_status(self, health_df):
        """
        Assign HEALTH / WARNING / CRITICAL status
        using service-specific thresholds.
        """ 

        rows = health_df.collect()

        output = []

        for row in rows:

            service = row["service"]

            thresholds = SERVICE_THRESHOLDS.get(
                service,
                {}
            )

            latency_warning = thresholds.get(
                "latency_warning",
                DEFAULT_THRESHOLDS["latency"]["warning"]
            )

            latency_critical = thresholds.get(
                "latency_critical",
                DEFAULT_THRESHOLDS["latency"]["critical"]
            )

            error_warning = thresholds.get(
                "error_rate_warning",
                DEFAULT_THRESHOLDS["error_rate"]["warning"]
            )

            error_critical = thresholds.get(
                "error_rate_critical",
                DEFAULT_THRESHOLDS["error_rate"]["critical"]
            )

            avg_latency = row["avg_latency_ms"]
            error_rate = row["error_rate"]

            # Health Status
            if (
                avg_latency >= latency_critical
                or error_rate >= error_critical
            ):
                status = "CRITICAL"

            elif (
                avg_latency >= latency_warning
                or error_rate >= error_warning
            ):
                status = "WARNING"

            else:
                status = "HEALTHY"

            # Health Score
            score = 100

            score -= min(error_rate, 50)

            score -= min(avg_latency / 100, 50)

            score = max(round(score, 2), 0)

            output.append({

                "service": service,

                "total_requests": row["total_requests"],

                "failed_requests": row["failed_requests"],

                "error_rate": row["error_rate"],

                "availability": row["availability"],

                "avg_latency_ms": row["avg_latency_ms"],

                "max_latency_ms": row["max_latency_ms"],

                "health_score": score,

                "health_status": status

            })

        return output

    def print_report(self, report):

        print("\n")
        print("=" * 100)
        print("SERVICE HEALTH REPORT")
        print("=" * 100)

        for service in report:

            print(f"""
                    Service            : {service['service']}
                    Health Status      : {service['health_status']}
                    Health Score       : {service['health_score']}

                    Total Requests     : {service['total_requests']}
                    Failed Requests    : {service['failed_requests']}

                    Average Latency    : {service['avg_latency_ms']} ms
                    Maximum Latency    : {service['max_latency_ms']} ms

                    Error Rate         : {service['error_rate']} %
                    Availability       : {service['availability']} %
                    """)

            print("-" * 100)




