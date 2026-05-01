-- Lists all records with a name in the table second_table
-- Results display score and name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;