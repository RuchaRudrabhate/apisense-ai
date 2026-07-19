#Wrapper file to test all the functionalities from platform_analytics

"""
Runs all Platform Analytics modules.

Current Modules
---------------
1. Service Health Analyzer
2. Traffic Analyzer

Future Modules
--------------
3. Anomaly Detector
4. Dependency Analyzer
5. Incident Detector
"""

from pyspark_jobs.log_parser import LogParser

from platform_analytics.service_health import ServiceHealthAnalyzer
from platform_analytics.traffic_analysis import TrafficAnalyzer


class PlatformAnalyticsRunner:

    def __init__(self):

        parser = LogParser()

        logs_df = parser.read_logs("datasets/logs.json")

        self.df = parser.parse_timestamps(logs_df)

   

    def run_service_health(self):

        print("\n")
        print("=" * 120)
        print("RUNNING SERVICE HEALTH ANALYZER")
        print("=" * 120)

        analyzer = ServiceHealthAnalyzer(self.df)

        health_df = analyzer.calculate_service_health()

        report = analyzer.assign_health_status(
            health_df
        )

        analyzer.print_report(report)

   

    def run_traffic_analysis(self):

        print("\n")
        print("=" * 120)
        print("RUNNING TRAFFIC ANALYZER")
        print("=" * 120)

        analyzer = TrafficAnalyzer(self.df)

        analyzer.total_requests()

        analyzer.requests_per_service()

        analyzer.requests_per_endpoint()

        analyzer.requests_per_method()

        analyzer.requests_per_region()

        analyzer.requests_per_host()

        analyzer.hourly_traffic()

        analyzer.daily_traffic()

        analyzer.peak_traffic_hour()

        analyzer.lowest_traffic_hour()

        analyzer.busiest_endpoint()

        analyzer.busiest_service()

        analyzer.traffic_share_per_service()

        analyzer.requests_per_status_code()

   

    def run_all(self):

        self.run_service_health()

        self.run_traffic_analysis()


if __name__ == "__main__":

    runner = PlatformAnalyticsRunner()

    runner.run_all()