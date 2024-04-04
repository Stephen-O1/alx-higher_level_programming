-- list number of score and occurrence with each score with number
-- data should be displayed in descending order

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
