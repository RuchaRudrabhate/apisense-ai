"""
Purpose: Analyze request traffic.

example - 
- Requests/hour
- Peak traffic
- Low traffic
- Traffic spikes
- Request trend
- Busiest endpoint
"""

from pyspark.sql.functions import (
    col,
    count,
    desc,
    hour,
    to_date,
    round
)

from platform_analytics.base_analyzer import BaseAnalyzer


class TrafficAnalyzer(BaseAnalyzer):

    def __init__(self, dataframe):
        super().__init__(dataframe)


    # 1. Total Requests


    def total_requests(self):

        total = self.df.count()

        print("\n========== TOTAL REQUESTS ==========\n")
        print(f"Total Requests : {total}")

        return total


    # 2. Requests Per Service


    def requests_per_service(self):

        print("\n========== REQUESTS PER SERVICE ==========\n")

        result = (
            self.df
            .groupBy("service")
            .count()
            .orderBy(desc("count"))
        )

        result.show(truncate=False)

        return result


    # 3. Requests Per Endpoint


    def requests_per_endpoint(self):

        print("\n========== REQUESTS PER ENDPOINT ==========\n")

        result = (
            self.df
            .groupBy("endpoint")
            .count()
            .orderBy(desc("count"))
        )

        result.show(truncate=False)

        return result


    # 4. Requests Per HTTP Method


    def requests_per_method(self):

        print("\n========== REQUESTS PER METHOD ==========\n")

        result = (
            self.df
            .groupBy("method")
            .count()
            .orderBy(desc("count"))
        )

        result.show()

        return result


    # 5. Requests Per Region


    def requests_per_region(self):

        print("\n========== REQUESTS PER REGION ==========\n")

        result = (
            self.df
            .groupBy("region")
            .count()
            .orderBy(desc("count"))
        )

        result.show(truncate=False)

        return result


    # 6. Requests Per Host


    def requests_per_host(self):

        print("\n========== REQUESTS PER HOST ==========\n")

        result = (
            self.df
            .groupBy("host")
            .count()
            .orderBy(desc("count"))
        )

        result.show(truncate=False)

        return result


    # 7. Hourly Traffic Trend


    def hourly_traffic(self):

        print("\n========== HOURLY TRAFFIC ==========\n")

        result = (
            self.df
            .withColumn("hour", hour(col("timestamp")))
            .groupBy("hour")
            .count()
            .orderBy("hour")
        )

        result.show(24, truncate=False)

        return result


    # 8. Daily Traffic Trend


    def daily_traffic(self):

        print("\n========== DAILY TRAFFIC ==========\n")

        result = (
            self.df
            .withColumn("date", to_date(col("timestamp")))
            .groupBy("date")
            .count()
            .orderBy("date")
        )

        result.show(truncate=False)

        return result
    
    # 9. PEAK TRAFFIC HOUR

    def peak_traffic_hour(self):

        print("\n========== PEAK TRAFFIC HOUR ==========\n")

        result = (
            self.df
            .withColumn("hour", hour(col("timestamp")))
            .groupBy("hour")
            .count()
            .orderBy(desc("count"))
            .limit(1)
        )

        result.show(truncate=False)

        return result
    
    #10. Lowest Traffic Hour
    def lowest_traffic_hour(self):

        print("\n========== LOWEST TRAFFIC HOUR ==========\n")

        result = (
            self.df
            .withColumn("hour", hour(col("timestamp")))
            .groupBy("hour")
            .count()
            .orderBy("count")
            .limit(1)
        )

        result.show(truncate=False)
        return result
    
    # 11. Busiest Endpoint
    def busiest_endpoint(self):
        print("\n========== BUSIEST ENDPOINT ==========\n")
        result = (
            self.df
            .groupBy("endpoint") 
            .count() 
            .orderBy(desc("count")) 
            .limit(1)
        )

        result.show(truncate = False)
        return result
    
    #12. Most Active Service

    def busiest_service(self):

        print("\n========== BUSIEST SERVICE ==========\n")

        result = (
            self.df
            .groupBy("service")
            .count()
            .orderBy(desc("count"))
            .limit(1)
        )
        result.show(truncate = False)
        return result
    
    #13 - Traffic Share Per Service
    def traffic_share_per_service(self):

        print("\n========== TRAFFIC SHARE PER SERVICE ==========\n")

        total_requests = self.df.count()

        result = (
            self.df
            .groupBy("service")
            .count()
            .withColumn(
                "traffic_percent",
                round((col("count") / total_requests) * 100, 2)
            )
            .orderBy(desc("traffic_percent"))
        )

        result.show(truncate=False)

        return result
    
    #14. Requests Per Status Code
    def requests_per_status_code(self):

        print("\n========== REQUESTS PER STATUS CODE ==========\n")
    
        result = (
            self.df
            .groupBy("status_code")
            .count()
            .orderBy("status_code")
        )
    
        result.show(truncate=False)
    
        return result