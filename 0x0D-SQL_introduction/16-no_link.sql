-- Lists all records of the table of the database
-- Don't list rows without a name value
-- results should display the score and the name
-- records sould be listed by descending order

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
