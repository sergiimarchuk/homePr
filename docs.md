
### ..doc..

#### run docker-composer
##### example: docker-compose -f /path/to/your/docker-compose.yml up -d 
```bash
docker-compose up -d


#### run 
```bash
sergii@smu-22:~$ psql -h localhost -p 5435 -U postgres -d postgres
Password for user postgres: 
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 13.15 (Debian 13.15-1.pgdg120+1))
Type "help" for help.

postgres=# 

#### run these to create tables and schema in container if you have no any backup etc, otherwise skip it

```

```bash
CREATE SCHEMA my_schema;

CREATE TABLE my_schema.table_count_data (
    id_count_data SERIAL PRIMARY KEY,
    counter_data BIGINT NOT NULL,
    date DATE NOT NULL,
    description TEXT
);

CREATE TABLE my_schema.table_picture_counter_data (
    id_picture SERIAL PRIMARY KEY,
    name_of_picture TEXT NOT NULL,
    id_count_data INTEGER NOT NULL REFERENCES my_schema.table_count_data(id_count_data),
    refer_mongo_entry TEXT,
    additional_info TEXT
);

```

#### run these commands if it neccessary, just depends on and up to you 

```bash
postgres=# \dt
Did not find any relations.
postgres=# \dn
   List of schemas
   Name    |  Owner   
-----------+----------
 my_schema | postgres
 public    | postgres
(2 rows)

postgres=# SET search_path TO my_schema;
SET
postgres=# 

SELECT * FROM my_schema.my_table;


postgres=# \dt
                     List of relations
  Schema   |            Name            | Type  |  Owner   
-----------+----------------------------+-------+----------
 my_schema | table_count_data           | table | postgres
 my_schema | table_picture_counter_data | table | postgres
(2 rows)

postgres=# 



INSERT INTO my_schema.table_count_data (counter_data, date, description)
VALUES (12345, '2023-06-07', 'Counter data for today');


INSERT INTO my_schema.table_picture_counter_data (name_of_picture, id_count_data, refer_mongo_entry, additional_info)
VALUES ('picture_001.jpg', (SELECT id_count_data FROM my_schema.table_count_data WHERE date = '2023-06-07'), 'mongo_entry_123', 'Additional information about the picture');



INSERT INTO table_count_data (counter_data, date, description)
VALUES (0326079, '2023-02-14', 'Feb 14 2024');


INSERT INTO table_picture_counter_data (name_of_picture, id_count_data, refer_mongo_entry, additional_info)
VALUES ('picture_001.jpg', (SELECT id_count_data FROM table_count_data WHERE date = '2023-02-14'), 'mongo_entry_123', 'The fist picture with data lectro counter');



