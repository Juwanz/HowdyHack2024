#!/usr/bin/env python
import pandas as pd
from faker import Faker
from sqlalchemy import create_engine, text
import random

# Initialize Faker with the 'en_US' locale for US-specific data
fake = Faker('en_US')

# Number of rows to generate
num_rows = 100  # Adjust as needed

# Function to generate a name based on gender
def generate_name_by_gender(gender):
    if gender == 'male':
        return fake.first_name_male(), fake.last_name()
    else:
        return fake.first_name_female(), fake.last_name()

# Function to create email from first and last name
def generate_email(first_name, last_name):
    # Create email in format: first.last@example.com
    domain = random.choice(['gmail.com', 'tamu.edu'])  # Random domain
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"

# Generate fake data
data = {
    'gender': [random.choice(['male', 'female','male','female','male', 'female','male','female','male', 'female','male','female', 'other/prefer not to say']) for _ in range(num_rows)],  # Randomly choose gender
    'first_name': [],  # This will be filled based on gender
    'last_name': [],   # Last name
    'age': [random.randint(18, 25) for _ in range(num_rows)],  # Age between 18 and 25
    'phone_number': [fake.numerify('(###) ###-####') for _ in range(num_rows)]  # US phone numbers
}

# Populate the 'first_name' and 'last_name' fields based on gender
for gender in data['gender']:
    first_name, last_name = generate_name_by_gender(gender)
    data['first_name'].append(first_name)
    data['last_name'].append(last_name)

# Generate email based on first_name and last_name
data['email'] = [generate_email(first_name, last_name) for first_name, last_name in zip(data['first_name'], data['last_name'])]

# Combine first_name and last_name into full name
data['name'] = [f"{first_name} {last_name}" for first_name, last_name in zip(data['first_name'], data['last_name'])]

# Create DataFrame
df = pd.DataFrame(data)

# Create an in-memory SQLite database
engine = create_engine('sqlite:///userData.db')

# Save DataFrame to SQL table
df.to_sql('user_data', engine, index=False, if_exists='replace')

# Query the table to see the results
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM user_data LIMIT 5"))
    for row in result:
        print(row)
