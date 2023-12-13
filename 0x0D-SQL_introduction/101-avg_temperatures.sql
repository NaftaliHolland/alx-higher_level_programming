-- Display the average temperature by city

SELECT `city`, AVG(`value`) AS "avg_temp"
FROM BY `city`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
