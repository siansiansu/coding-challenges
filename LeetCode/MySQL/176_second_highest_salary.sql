# Write your MySQL query statement below
SELECT MAX(t1.Salary) AS SecondHighestSalary
  FROM Employee AS t1
 WHERE t1.Salary < (SELECT MAX(t1.Salary) AS SecondHighestSalary
                     FROM Employee AS t1);