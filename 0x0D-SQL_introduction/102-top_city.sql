-- Display the average temperature by city

SELECT `city`, AVG(`value`) AS "avg_temp"
FROM `temperatures` WHERE `month` BETWEEN 7 and 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
