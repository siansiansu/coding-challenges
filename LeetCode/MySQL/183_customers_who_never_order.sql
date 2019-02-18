# Write your MySQL query statement below
SELECT Name AS Customers
  FROM Customers AS e1
       LEFT JOIN Orders AS e2
       ON e1.Id = e2.CustomerId
 WHERE e2.CustomerId is NULL;