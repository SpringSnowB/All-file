alter table book
add brief text;


update book set price = 45
where title ='史记';

alter table book
add publication_time date ;

update book set publication_time ='2012-1-16'
where title = '骆驼祥子';

update book set publication_time ='1990-8-16'
where title = '茶馆';

delete from book
where publication_time < '2000-1-1';

--正则表达式
 select * from cls
 where name regexp '^p.+';

 select * from cls
 order by age,score;

 select * from cls
 order by age,score desc;

-- 1. 创建表 sanguo
-- 2. 表结构如下
--id  name  gender  country
--attack（>100）  defense(0-100)
create table sanguo
(id int primary key auto_increment,
name char(12) not null,
gender char(3) not null,
country enum('魏','蜀','吴') not null,
attack smallint default 100,
defense tinyint default 20);


--3. 插入数据
--   魏：司马懿  夏侯渊  张辽  曹操 甄姬
--  蜀：赵云 孙尚香 诸葛亮 张飞 关羽
--   吴：周瑜 小乔  大乔  陆逊  鲁肃

insert into sanguo values
(1,'司马懿','6','魏',250,60),
(2,'赵云','12','蜀',850,85),
(3,'夏侯渊','12','魏',630,43),
(4,'孙尚香','8','蜀',285,63),
(5,'张辽','7','魏',444,75),
(6,'诸葛亮','11','蜀',276,45),
(7,'曹操','16','魏',562,82),
(8,'张飞','14','蜀',600,80),
(9,'甄姬','6','魏',240,13),
(10,'关羽','16','蜀',640,62),
(11,'周瑜','6','吴',380,28),
(12,'小乔','6','吴',277,54),
(13,'大乔','10','吴',456,71),
(14,'陆逊','9','吴',299,90),
(15,'鲁肃','2','吴',150,86);


--4. 查找
--   查找所有蜀国人信息
 select * from sanguo
 where country ='蜀';

--   将赵云的攻击力设为360,防御力设置为68
update sanguo
set attack =360,defense = 68
where name = '赵云';

-- 将吴国英雄攻击力超过300的 改为300，防御力改为65
update sanguo s
et attack = 300,defense = 65
where country = '吴' and attack >= 300;

-- 查找攻击力高于250的蜀国英雄的名字和攻击力
select name,attack from sanguo
where country = '蜀' and attack>=250;

-- 将所有英雄攻击力按从高到底排名，如果攻击力相同则按照防御力从高到底排名
select * from sanguo
order by attack desc,defense desc;

-- 将魏蜀两国英雄名字为三个字的按照防御力升序排序
select * from sanguo
where country in ('魏','蜀') and name like "___"
order by defense;
-- 找到吴国英雄中攻击力排名前2的
select * from sanguo
where country ='吴'
order by attack desc
limit 2;

--找出蜀国中攻击力大于魏国攻击力最高的英雄
select * from sanguo
where country = '蜀' and
attack > (
select max(attack) from sanguo
where country = '魏')
);

select * from sanguo
where country = '蜀' and attack >
( select attack from sanguo
where country = '魏'
order by attack desc
limit 1);

select avg(attack) as 攻击力平均值
from sanguo where country = '蜀';

select sum(defense) from sanguo
where country = '蜀';

select count(*) from sanguo
where country = '蜀';

select count(*) from sanguo
where attack> 300;

select country,avg(attack) as 平均攻击力 from sanguo
group by country;

select gender,count(*) from sanguo
group by gender;

select country,gender,avg(attack) from sanguo
group by country,gender;--按照多个字段进行分组

--升序
select country,count(*) from sanguo
where gender = '男'
group by country
order by count(*) limit 2;
--降序  所有国家中，男英雄比较多的前两个国家的国家姓名和男英雄数量
select country,count(*) from sanguo
where gender = '男'
group by country
order by count(*) desc
limit 2;

select country,avg(attack) from sanguo
group by country
having avg(attack)>200
order by avg(attack) desc
limit 2;

create table index_test
(id int auto_increment,
name varchar(20),
primary key(id),
 index(name));

drop index name on index_test;--删除索引