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


-- 1965. Employees With Missing Information: (https://leetcode.com/problems/employees-with-missing-information/description/?envType=study-plan&id=sql-i)
-- when we want to use outer join, we cannot use it in mysql, instead we use union of left join and right join
-- when you do that, make sure that you are using 'using' clause instead of on, as we can't use duplicated on clause for union
select T.employee_id
from (select * from Employees left join Salaries using(employee_id)
    union 
    select * from Employees right join Salaries using(employee_id)) as T
where T.name is null or T.salary is null
order by T.employee_id;


-- 1795. Rearrange Products Table: (https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan&id=sql-i)
-- when you want to append the result row-wise, consider using 'union' of three select * 
select product_id, 'store1' as store, store1 as price from Products where store1 is not null
union
select product_id, 'store2' as store, store2 as price from Products where store2 is not null
union
select product_id, 'store3' as store, store3 as price from Products where store3 is not null;   



-- 608. Tree Node: (ttps://leetcode.com/problems/tree-node/description/?envType=study-plan&id=sql-i)
-- case when then, when then, else end == if elif else
select id, 
case 
when p_id is null then 'Root'
when id in (select p_id from Tree) then 'Inner' 
else 'Leaf'
end as type
from Tree;