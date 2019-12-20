create function (id1 int,id2 int) returns int
begin
set @a = (select score from cls where id = id1);
set @b = (select score from cls where id = id2);
return @a-@b;
end //



create procedure get_age(in sid int,out num int)
begin declare val int;
select age from cls where id =sid into val;
set num =val;
end//