from pyspark.sql import DataFrame

class BaseAnalyzer:
    """
    Base Analyzer class that can be reused by other analytical modules.
    Provides common Spark DataFrame operations.
    """
    def __init__(self, dataframe):
        """
        Initialize the base class
        Args:
            dataframe: Parsed Spark DataFrame.
        """
        self.df = dataframe

    def validate_dataframe(self):
        """
        validates the input dataframe exists and non empty

        raises:
            ValueError
        """

        if self.df is None:
            raise ValueError("Input DataFrame is None.")
        elif self.df.rdd.isEmpty():
            raise ValueError("Input Dataframe is empty.")
        
    def total_records(self):
        """
        Returns total number of records.
        """

        return self.df.count()
    
    def show_schema(self):
        """
        returns schema
        """

        print("\n------ Dataframe Schema ------\n")
        self.df.printSchema()
    
    def show_sample_data(self, rows = 10):
        """
        print sample rows
        """
        print(f"\n------ FIRST {rows} RECORDS ------\n")
        self.df.show(rows, truncate=False)
    
    def cache_dataframe(self):

        """
        Cache DataFrame in memory for faster repeated operations.
        """

        self.df.cache()

    def unpersist_dataframe(self):
        """
        Remove DataFrame from cache.
        """
        self.df.unpersist()

    def dataframe_columns(self):
        """
        Returns list of DataFrame columns.
        """
        return self.df.columns