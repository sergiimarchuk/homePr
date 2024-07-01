#!/bin/bash

source config.sh

# Database connection details
host="localhost"
port="5435"
username="postgres"
database="postgres"
#password="123456"
password="$DB_PASSWORD"

# Get the arguments from the command line
counter_data=$1
date=$2
description=$3

# Check if the arguments are null and set default values if necessary
counter_data=${counter_data:-null}
date=${date:-null}
description=${description:-null}

# Enclose string values in single quotes
if [ "$date" != "null" ]; then
    date="'$date'"
fi
if [ "$description" != "null" ]; then
    description="'$description'"
fi

# INSERT query to add data to the table
insert_query="INSERT INTO my_schema.table_count_data (counter_data, date, description) VALUES ($counter_data, $date, $description);"

# SELECT query to retrieve data from the table
select_query="SELECT * FROM my_schema.table_count_data;"

# Set the PGPASSWORD environment variable
export PGPASSWORD="$password"

# Execute the INSERT query using psql command
psql -h "$host" -p "$port" -U "$username" -d "$database" -w -c "$insert_query"

echo "Data inserted successfully!"

# Execute the SELECT query using psql command
psql -h "$host" -p "$port" -U "$username" -d "$database" -w -c "$select_query"
