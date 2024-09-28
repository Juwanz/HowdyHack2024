#!/usr/bin/env python
import pandas as pd
from faker import Faker
from sqlalchemy import create_engine, text  # Import the `text` function
import random

# Initialize Faker
fake = Faker()

# Number of rows to generate
num_rows = 100  # you can adjust this

# Generate fake data
data = {
    'email': [fake.email() for _ in range(num_rows)],
    'password': [fake.password(length=10) for _ in range(num_rows)],  # passwords with length of 10 characters
    'name': [fake.name() for _ in range(num_rows)],
    'age': [random.randint(18, 80) for _ in range(num_rows)]  # age between 18 and 25
}

# Create DataFrame
df = pd.DataFrame(data)

# Create an in-memory SQLite database or connect to any other database (e.g., MySQL, PostgreSQL, etc.)
engine = create_engine('sqlite:///user_data.db')

# Save DataFrame to SQL table
df.to_sql('user_data', engine, index=False, if_exists='replace')

# Query the table to see the results
with engine.connect() as connection:
    # Use `text()` to wrap the SQL query
    result = connection.execute(text("SELECT * FROM user_data LIMIT 5"))
    
    for row in result:
        print(row)














   
   
   













 


