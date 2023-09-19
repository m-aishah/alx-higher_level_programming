-- Lists all records with a score >= 10 in the table second_table
-- Displays both the score and name with scores in descending order.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
