DELETE FROM Person 
WHERE ID NOT IN 
(SELECT * FROM (SELECT MIN(Id)
                FROM Person p
                GROUP BY Email) t);