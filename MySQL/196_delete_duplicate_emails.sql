# Write your MySQL query statement below
DELETE e2 
  FROM Person AS e1, Person AS e2
 WHERE e1.Email = e2.Email 
   AND e2.Id > e1.Id;