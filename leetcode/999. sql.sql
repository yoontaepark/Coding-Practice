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


-- 1667. Fix Names in a Table: (https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan&id=sql-i)
-- : use concat(A,B) // also left(upper(A), 1) makes left first letter upper 
select user_id, concat(left(upper(name), 1), right(lower(name), length(name)-1)) as name
from Users
order by user_id;


-- 1484. Group Sold Products By The Date: (https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan&id=sql-i)
-- : use group_concat(~~~ separator ',')  그룹핑하면서 리스트로 나열하고 싶을때 사용
select sell_date, 
       count(distinct product) as num_sold, 
       group_concat(distinct product order by product separator ',') as products
from Activities
group by sell_date
order by sell_date;


-- 1527. Patients With a Condition: https://leetcode.com/study-plan/sql/?progress=xixtwdh7#:~:text=1527.%20Patients%20With%20a%20Condition
-- name like '%something' or 'something%' when we want to track some substrings 
select patient_id, patient_name, conditions
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%';