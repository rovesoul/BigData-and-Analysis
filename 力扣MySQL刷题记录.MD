刷题记录
每道题,自己思路一个,吸取评论区思路一个,若和评论区答案差不多一样,则保留一个

```sql
-- https://leetcode-cn.com/problems/big-countries/
select name , population,area from World where area>3000000 or population> 25000000;

--https://leetcode-cn.com/problems/classes-more-than-5-students/solution/
select class from courses group by class having count(distinct student)>=5 ;

--https://leetcode-cn.com/problems/duplicate-emails/submissions/
--知道使用group by和having。还需要记得优先顺序。where>group by>having>order by
--两种方法都实现了
select Email from Person group by Email having count(distinct Id)>1 ;
select Email from Person group by Email having count(Email) >=2

--https://leetcode-cn.com/problems/not-boring-movies/
select * from cinema where id%2 !=0 and description != 'boring' order by rating desc;
select * from cinema where description <> 'boring' and mod(id,2)=1 order by rating desc;

--https://leetcode-cn.com/problems/swap-salary/
update salary set sex=if(sex = 'f', 'm','f');


--https://leetcode-cn.com/problems/combine-two-tables/
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId

--https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/
-- 没做出来,看解析学的答案
select a.name as Employee
from employee a inner join employee b on a.managerid = b.id 
and a.salary > b.salary

--https://leetcode-cn.com/problems/delete-duplicate-emails/solution/
DELETE p1 
FROM Person as p1 , Person as p2
WHERE p1.Email = p2.Email  AND p1.Id > p2.Id

--
--我写了一个不用转化data的,但这个错了.因为给的样例中id随日期列增加,但是测试集 id随着 日期反序排列
select w1.id
from weather w1,weather w2  
where w1.id= w2.id+1  and w1.temperature  > w2.temperature 

--需要改变日期格式后的对比代码'datediff'
SELECT weather.id AS 'Id'
FROM weather JOIN weather w ON DATEDIFF(weather.recorddate, w.recorddate) = 1  AND weather.Temperature > w.Temperature

--https://leetcode-cn.com/problems/second-highest-salary/submissions/
select max(Salary) as SecondHighestSalary from Employee 
where Salary<(select max(Salary) from Employee)
```
更新日期:2019/11/24
