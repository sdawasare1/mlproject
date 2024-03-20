Emp = Name, Salary

maximum salary - 

select name, salary from employee
order by salary desc

select * from employee where salary in (select name, salary from employee order by salary desc) 


select e1.name, e1.salary from employee e1
self join employee e2 on e1.name = e2.name
where e1.salary 


select name from employee 
where salary%2 