select e.Name as Employee from Employee e inner join Employee m on e.ManagerId = m.Id and e.Salary > m.Salary
