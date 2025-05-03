
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize contexts
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load the movies dataset from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket-name/raw/movies.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

# Clean the data: Remove nulls and drop duplicates
cleaned_data = datasource.drop_nulls().drop_duplicates()

# Transformation: Calculate average rating by genre
df = cleaned_data.toDF()
df.createOrReplaceTempView("movies")

avg_rating_by_genre = spark.sql("""
    SELECT genre, ROUND(AVG(CAST(rating AS FLOAT)), 2) as avg_rating
    FROM movies
    GROUP BY genre
    ORDER BY avg_rating DESC
""")

# Convert to DynamicFrame for Glue
transformed_data = DynamicFrame.fromDF(avg_rating_by_genre, glueContext, "transformed_data")

# Write the output to another S3 location in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=transformed_data,
    connection_type="s3",
    connection_options={"path": "s3://your-bucket-name/processed/movies_avg_rating_by_genre/"},
    format="parquet"
)

job.commit()
