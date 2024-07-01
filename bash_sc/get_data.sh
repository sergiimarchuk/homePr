#!/bin/bash

# Database connection details
host="localhost"
port="5435"
username="postgres"
database="postgres"
password="123456"

# Query to retrieve data from the table
query="SELECT * FROM my_schema.table_count_data;"

export PGPASSWORD="$password"

# Execute the query using psql command
psql -h "$host" -p "$port" -U "$username" -d "$database" -c "$query" 




#<<EOF
#$password
#EOF
