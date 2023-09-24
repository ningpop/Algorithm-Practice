CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare a int;
    set a = N - 1;
    RETURN (
        # Write your MySQL query statement below
        select distinct E.salary from Employee E order by E.salary desc limit a, 1
    );
END