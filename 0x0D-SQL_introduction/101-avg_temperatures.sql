-- Displays the average temperature by city ordered in descending order by temperature.
SELECT `city`, AVG(`values`) AS `avg_temp` FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
