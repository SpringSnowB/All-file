create table `class_1`(
`id` int primary key auto_increment,
`name` varchar(32) not null ,
`age` tinyint unsigned not null ,
`sex` enum('m','w','o'),
`score` float default 0
);
create table `interest`(
`id` int primary key auto_increment,
`name` varchar(32) not null ,
`hobby` varchar(100),
`level` char ,
`price` decimal(7,2),
`remark` text
);

insert into class_1
values (1,'kk',18,'m',89);

insert into class_1
values (2,'ww',19,'w',78),
(3,'ee',19,'w',96);

insert into interest values
(1,'kk','sing,dance','b',5800.00,'interesting');

insert into interest values
(3,'ee','drink','c',5600.55,'boring'),
(4,'pp','draw','a',3890.00,'wonderfull');

insert into class_1(name,age,sex)
values('pp',19,'m');

create database books charset=utf8;
create table book(
`id` int primary key auto_increment,
`title` varchar(32) not null,
`author` varchar(32) not null ,
`price` decimal(5,2) not null ,
`publication` varchar(64) not null,
`comment` text
);

insert into book values
(1,'史记','司马迁',39.80,'中国教育','中国古代第一步编年著作'),
(2,'天蓝色的彼岸','亚历克斯?希勒',34.50,'人民教育','儿童读物'),
(3,'Python编程入门','佚名',64.60,'机械工业','python程序员入门读物'),
(4,'茶馆','老舍',35.63,'中国教育','老舍经典著作'),
(5,'鬼谷子','鬼谷子',74.50,'人民教育','一身受益必读'),
(6,'数据结构','严蔚敏',44.80,'机械工业','原理'),
(7,'素描基础教程','佚名',37.20,'人民教育','绘画基础'),
(8,'数据仓库','唐朝',68.20,'机械工业','数据挖掘技术衍生读物'),
(9,'秘密花园','佚名',36.90,'中国教育','儿童读物');

--查找所有价格30多的书
 select title from book
 where price >=30 and price <40;

 --查找出版社为中国教育的
 select title from book
 where publication ='中国教育';

 --查找老舍写的中国教育出版社的
 select title from book
 where publication ='中国教育' and author = '老舍';

 --查找备注不为空的
 select title from book
 where comment is null;

 --查找所有价格大于60的，只看书名和价格
 select title,price from book where price>60;

 --查找作者是XX或者XX的书
 select title from book
 where author in ('老舍','司马迁');--in的效率比or要高

insert into book(title,author,price,publication)
values('朝花夕 拾','鲁讯',45.80,'人民教育'),
('骆驼祥子','老舍',36.70,'人民教育');

