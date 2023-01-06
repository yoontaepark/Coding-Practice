-- Lc 1873. Calculate Special Bonus: (https://leetcode.com/problems/calculate-special-bonus)
-- : case when * then * else * end 예제 
select employee_id, 
case when (employee_id % 2 != 0) and (left(name, 1) not in ('M')) then salary else 0 end as bonus
from Employees
order by employee_id;

-- 627. Swap Salary: (https://leetcode.com/problems/swap-salary/)
-- : prepare for update line question
update Salary set sex= 
case
when sex='f' then 'm'
when sex='m' then 'f'
end;

-- 196. Delete Duplicate Emails: (https://leetcode.com/problems/delete-duplicate-emails/)
-- : good to know method to call two same table and remove by condition 
delete p1
from Person as p1, Person as p2
where p1.email = p2.email and p1.id > p2.id;
