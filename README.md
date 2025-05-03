# AWS Data Pipeline – End-to-End Hands-On Project

This project demonstrates the design and implementation of a complete AWS-based ETL data pipeline. It extracts movie data from a raw CSV file, transforms it using AWS Glue, and loads the processed data into Amazon Redshift for analytics and reporting.

## 🚀 Project Overview

- **Data Source**: IMDB Top 250 Movies CSV file  
- **ETL Engine**: AWS Glue (PySpark job)
- **Data Storage**: Amazon S3 (raw and processed data)
- **Data Warehouse**: Amazon Redshift
- **Orchestration**: AWS Glue Workflow and Triggers

## 🧰 Tech Stack

- **AWS Services**: S3, Glue, Redshift
- **Programming**: Python (PySpark)
- **SQL**: Redshift-compatible SQL queries
- **Visualization**: Redshift table views and data snapshots


## ⚙️ Steps Performed

1. **Upload Raw Data** to S3
2. **Create AWS Glue Job** using PySpark to process the data
3. **Transform and Write Processed Data** back to S3
4. **Create Redshift Table** and load data using `COPY` command
5. **Query & Validate Results** with SQL scripts

## 📸 Sample Output

- ✅ Glue job success
- 📊 Redshift table showing processed movie data
- 🪣 S3 bucket with processed data in Parquet format

## 📌 Key Learnings

- Real-world usage of Glue ETL jobs for batch processing
- Data lake architecture using AWS S3
- Loading transformed data into Redshift for analytics
- SQL performance and optimization with large datasets



