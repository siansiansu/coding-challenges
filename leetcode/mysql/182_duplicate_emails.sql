# Write your MySQL query statement below
SELECT Email
  FROM Person AS e1
 GROUP BY Email
HAVING COUNT(*) > 1