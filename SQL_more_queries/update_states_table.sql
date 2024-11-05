-- Use the specified database
USE hbtn_0d_usa;

-- Remove duplicates, keeping only the row with the lowest id for each state name
DELETE s1
FROM states s1
INNER JOIN states s2
ON s1.name = s2.name
WHERE s1.id > s2.id;

-- Add a unique constraint on the name column to prevent future duplicates
ALTER TABLE states ADD CONSTRAINT unique_name UNIQUE (name);
