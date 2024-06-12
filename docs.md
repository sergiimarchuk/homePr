
### ..doc..

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

