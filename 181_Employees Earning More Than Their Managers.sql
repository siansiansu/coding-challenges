SELECT T1.Name "Employee"
FROM Employee T1 , Employee T2
WHERE T1.ManagerId = T2.Id AND T1.Salary > T2.Salary