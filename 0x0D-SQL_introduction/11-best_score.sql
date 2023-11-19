-- Lists all records in the 'second_table' that has a score >= 10

SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
