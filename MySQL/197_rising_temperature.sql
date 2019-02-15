# Write your MySQL query statement below
SELECT a.Id
  FROM Weather a, Weather b
 WHERE DATEDIFF(a.RecordDate, b.RecordDate) = 1
   AND a.temperature > b.Temperature