-- Lists all the records of table second_table.
-- Displays only rows with a name value.
-- Displays the score and the name (in this order).
-- Records are listed in descending order by score.
SELECT `score`, `name` FROM `second_table` WHERE `name` != ""
ORDER BY `score` DESC;
