-- Lists all cities of California from the database hbtn_0d_usa
-- The script uses a subquery to find California's ID without using JOIN
SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC;