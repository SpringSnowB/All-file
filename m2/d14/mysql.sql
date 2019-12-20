create table user
(id int not null primary key auto_increment,
name char(20) not null  ,
age tinyint not null default 20,
sex enum('m','w') default 'm'
);

create table friend_circle
(id int not null primary key auto_increment,
uid int not null,
content text default null,
place char(20) default null,
posted_time datetime default now(),
picture text,
constraint user_fk foreign key(uid) references user(id)
);


create table comment_like(
id int not null primary key auto_increment,
uid int not null,
fid int not null,
dz enum('1','0') default '0',
comment text default null,
constraint use_fk foreign key(uid) references user(id),
constraint friend_fk foreign key(fid) references friend_circle(id)
);


create table stu
(
sid int primary key auto_increment,
name varchar(20),
age tinyint,
sex enum('m','w'),
native_place varchar(30)
);
create table teacher
(tid int primary key auto_increment,
name varchar(20),
age tinyint,
rank enum('讲师','副教授','教授')
);

create table course
(cid int primary key auto_increment,
name varchar(20),
credit decimal(2,1),
tid int,
constraint teacher_fk foreign key(tid) references teacher(tid)
);



create table chose_course
(id int primary key auto_increment,
sid int,
cid int,
socre decimal(3,1),
constraint student_fk foreign key(sid) references stu(sid),
constraint course_fk foreign key (cid) references course(cid)
);

--对book表进行重组
--分为  书籍表  作者表 和出版社表
--1. 通过ER模型规划三个表的内容和关系
--2. 设计三者之间的关系
--3. 根据你的设计创建三个表完善表关系

create table press
(pid int primary key auto_increment,
pname varchar(20),
address varchar(30),
phone char(11)
);

create table book
(bid int primary key auto_increment,
bname varchar(30),
publication_number smallint,
edition cahr(6),
publication_time date,
content text
);

create table writer
(wid int primary key auto_increment,
wname char(20),
age tinyint,
sex enum('m','w'),
country char(10),
phone char(11)
);

create table write
(bid int,
wid int,
write_time date ,
primary key(bid,wid),
constraint book_fk foreign key(bid) references book(bid),
constraint writer_fk foreign key(wid) references writer(wid)
);