#1-2
select a.s_id as s_id,score1,score2
from (
select s_id,score as score1
from score where c_id = '01'
) as a
inner join
(
select s_id,score as score2
from score where c_id ='02'
) as b
on a.s_id = b.s_id
where score1<score2;


#3-4
select student.s_id as id,
student.s_name as name,
s.avg_score as avg_score
from student
right join
(select s_id,avg(score) as avg_score
from score
group by s_id
having avg_score>60) as s
on student.s_id = s.s_id;


#5
select student.s_id as id,
student.s_name as name,
s.cnumber as cnumber,
s.csum as csum
from student
right join
(select s_id,count(s_id) as cnumber,sum(score) as csum
from score
group by s_id) as s
on student.s_id = s.s_id;

#6
select count(t_name) as number
from teacher
where t_name like "李%";

#7
select s_name,s_id,s_age,s_sex from total
where t_name ='张三';

#8
select * from student
where s_id not in
(select distinct s_id from total
where t_name = '张三');

#9
select * from student
where s_id in (select s_id from score where c_id = '01')
and s_id in (select s_id from score where c_id = '02');

#10
select * from student
where s_id in (select s_id from score where c_id = '01')
and s_id not in (select s_id from score where c_id = '02');

#11
select * from student
where s_id in
(select s_id from score
group by s_id
having count(s_id)<3);

#12
select * from student
where s_id in
(select distinct s_id from score -- 用distinct去重，提高查询效率
where c_id in
(select c_id from score
where s_id = '01'));

#13
select * from student
where s_id in(
select s_id from
(
select score.s_id as s_id,a.c_id as c_id from
(select c_id from score
where s_id = '01') as a
inner join score
on a.c_id = score.c_id
) b
where s_id <>'01'
group by s_id
having count(c_id)=
(select count(c_id) from score
where s_id='01'
));


#14
select s_name from student
where s_id not in
(select s_id from total
where t_name= '张三');


#15

select avg_sc.s_id,s_name,avg_sc.avg_score from
(select s_id as s_id,avg(score) as avg_score
from score
where score <60
group by s_id
having count(*) >=2) as avg_sc
left join student
on avg_sc.s_id = student.s_id;


#16

select s.s_id,s.s_name,s.s_age,s.s_sex,sc.score
from (select s_id,score from score
where score<60 and c_id ='01') as sc
left join student as s
on sc.s_id = s.s_id
order by sc.score desc;

#17

#21

select t_id,b.c_id,avg(sc) as avg_score from
(select score as sc,c_id from score ) as a right join
(select t.t_id as t_id,t_name,c_id from teacher as t,course as c)as b
on a.c_id = b.c_id
group by t_id,c_id
order by avg_score desc;

#22

#25
select

#26
select c_id,count(s_id)as 选课人数 from score
group by c_id;

#27
select s_id,s_name from student where s_id in
(select s_id from score
group by s_id
having count(c_id)=2);

#28
select s_sex,count(*) as 人数 from student group by s_sex;

#29
select * from student where s_name like "%风%";

#30
select s_name, count(s_id) from student group by s_name;

#31
select s_name from student where s_age like '1990%';

#32
select c_id,avg(score) as 平均成绩 from score
group by c_id
order by 平均成绩 desc,c_id;


#33
select s.s_id,s.s_name,avg_sc from
(select s_id,avg(score) as avg_sc from score
group by s_id having avg(score)>=85) a
left join student as s on a.s_id = s.s_id;

#34
select s_name,score from total
where c_name ='01' and score <60;

select student.s_name,score.score,c_name
from student,score,course
where student.s_id = score.s_id
and course.c_id = score.c_id
and c_name = '数学' and score <60;

#35
select s_id,c_id ,score from total
group by s_id,c_id,score;

#36
select s_name,c_id,score from total where score>70;

#37
select sc.c_id,c_name,score from score as sc
left join course as c
on sc.c_id = c.c_id where score<60;

#38
select s_id,s_name from student where s_id in
(select s_id from score where c_id ='01' and score >80);

#39
select count(s_id) as 人数 from score group by c_id;

#40
select student.*,score from
(select score,s_id from total
where t_name='张三' order by score desc limit 1) a
left join student on a.s_id = student.s_id;

#41
select a.* from score as a,score as b
where a.c_id = b.c_id
and a.s_id!=b.s_id
and a.score=b.score;

#42
(select c_id,s_id from score where c_id='01' order by score limit 2)
union
(select c_id,s_id from score where c_id='02' order by score limit 2)
union
(select c_id,s_id from score where c_id='03' order by score limit 2);


#43
select c_id,count(s_id) as 选修人数 from score
group by c_id
having 选修人数>5
order by 选修人数 desc,c_id;

#44
select s_id from score group by s_id having count(c_id)>2;

#45
pass

#46




