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

-- 176. Second Highest Salary: (https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan&id=sql-i)
-- ifnull (null, 아닐경우 값), LIMIT 행_갯수 OFFSET 시작행
select ifnull (null, 
(select distinct salary 
from Employee
order by salary desc
limit 1
offset 1)) as SecondHighestSalary;


-- 175. Combine Two Tables: (https://leetcode.com/problems/combine-two-tables/description/?envType=study-plan&id=sql-i)
-- warm up question (will remove later)
select p.firstName, p.lastName, a.city, a.state
from Person as p
left outer join Address as a 
on p.personId = a.personId;


-- 1581. Customer Who Visited but Did Not Make Any Transactions: (https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan&id=sql-i)
-- warm up question, but also good to look up before any coding tests
select v.customer_id, count(distinct v.visit_id) as count_no_trans from Visits as v
left outer join Transactions as t on v.visit_id = t.visit_id
where t.amount is null
group by v.customer_id;


-- 1148. Article Views I: https://leetcode.com/problems/article-views-i/description/?envType=study-plan&id=sql-i
-- this is one of good methods to go over 
select distinct author_id as id from Views
where author_id = viewer_id
order by id;

-- 197. Rising Temperature: https://leetcode.com/problems/rising-temperature/description/?envType=study-plan&id=sql-i
-- we can simply put two same tables not calling any join function, also remember to use to_days() function 
select w2.id as id
from Weather as w1, Weather as w2
where (to_days(w2.recordDate) - to_days(w1.recordDate) = 1)
and (w2.temperature > w1.temperature);


-- 607. Sales Person: https://leetcode.com/problems/sales-person/description/?envType=study-plan&id=sql-i
-- using multiple joins, and also think of not in statement 
select s.name as name from SalesPerson as s
where s.name not in (
    select s.name from SalesPerson as s
    left outer join Orders as o on s.sales_id = o.sales_id
    left outer join Company as c on o.com_id = c.com_id
    where c.name = 'RED'
)

-- 1141. User Activity for the Past 30 Days I: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan&id=sql-i
-- very simple question, and can ignore activity type 
select activity_date as day, count(distinct user_id) as active_users
from Activity
where to_days('2019-07-27') - to_days(activity_date) < 30 
and to_days('2019-07-27') - to_days(activity_date) >= 0
group by activity_date;

-- 1693. Daily Leads and Partners: https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan&id=sql-i
-- 굳이 넣어야?
select date_id, make_name, count(distinct lead_id) as unique_leads, 
count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name;


-- 586. Customer Placing the Largest Number of Orders: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=study-plan&id=sql-i
-- good to look once 
select customer_number
from Orders
group by customer_number
order by count(distinct order_number) desc
limit 1;


-- 511. Game Play Analysis I: https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan&id=sql-i
-- we can set min date to get the first date 
select player_id, min(event_date) as first_login
from Activity
group by player_id


-- 1890. The Latest Login in 2020: https://leetcode.com/problems/the-latest-login-in-2020/description/?envType=study-plan&id=sql-i
-- similar to upper question 
select user_id, max(time_stamp) as last_stamp
from Logins
where left(time_stamp, 4) = '2020'
group by user_id

-- 1741. Find Total Time Spent by Each Employee: https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/?envType=study-plan&id=sql-i
-- will remove this question 
select event_day as day, emp_id, sum(out_time - in_time) as total_time
from Employees
group by day, emp_id;
