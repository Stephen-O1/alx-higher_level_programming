-- create table; shouldn't fail if already exist

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
