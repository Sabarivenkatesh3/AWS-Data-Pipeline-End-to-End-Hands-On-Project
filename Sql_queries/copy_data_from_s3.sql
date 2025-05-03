COPY movies_avg_rating_by_genre
FROM 's3://project-123-sabari/processed/movies_avg_rating_by_genre/'
IAM_ROLE 'arn:aws:iam::<your-account-id>:role/<your-redshift-role>'
FORMAT AS PARQUET;
