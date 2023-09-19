-- Lists the number of records witht he same score in the table second_table.
SELECT `score`, COUNT(*) AS `number` 
FROM `second_table`
GROUP BY `score` 
ORDER BY `number` DESC;
