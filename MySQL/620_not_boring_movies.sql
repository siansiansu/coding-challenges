# Write your MySQL query statement below
SELECT *
  FROM cinema
 WHERE description != 'boring'
   AND Id % 2 != 0
 ORDER BY rating desc