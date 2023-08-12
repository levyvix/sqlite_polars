import polars as pl

# from sqlalchemy import create_engine


# engine = create_engine('sqlite:///database.db', echo=False)
# read from the sqlite database and write to csv

import time

start = time.time()
df = pl.read_database('select * from user;', connection_uri='sqlite://database.db')

(df
 .with_columns([
    pl.col("username").str.to_uppercase().alias("username_upper"),
    pl.col("password").str.to_lowercase().alias("password_lower")
 ])
 .write_csv("transformed_database.csv"))
end = time.time()
print("Time taken to transform to csv: ", end - start)