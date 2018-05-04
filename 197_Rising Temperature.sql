SELECT T1.id
FROM Weather T1, Weather T2
WHERE DATEDIFF(T1.RecordDate, T2.RecordDate) = 1 
AND T1.Temperature > T2.Temperature;