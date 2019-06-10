# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
  FROM Person t1
LEFT JOIN Address t2 ON t1.PersonId = t2.PersonId