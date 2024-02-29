set serveroutput on

create table instructor
	(ID			varchar(5), 
	 name			varchar(20) not null, 
	 dept_name		varchar(20), 
	 salary	numeric(8,2) check (salary > 29000),
	 primary key (ID),
	);
insert into instructor values ('10101', 'Srinivasan', 'Comp. Sci.', '65000');
insert into instructor values ('12121', 'Wu', 'Finance', '90000');
insert into instructor values ('15151', 'Mozart', 'Music', '40000');
insert into instructor values ('22222', 'Einstein', 'Physics', '95000');
insert into instructor values ('32343', 'El Said', 'History', '60000');
insert into instructor values ('33456', 'Gold', 'Physics', '87000');
insert into instructor values ('45565', 'Katz', 'Comp. Sci.', '75000');
insert into instructor values ('58583', 'Califieri', 'History', '62000');
insert into instructor values ('76543', 'Singh', 'Finance', '80000');
insert into instructor values ('76766', 'Crick', 'Biology', '72000');
insert into instructor values ('83821', 'Brandt', 'Comp. Sci.', '92000');
insert into instructor values ('98345', 'Kim', 'Elec. Eng.', '80000');

drop table salary_raise;

create table salary_raise(instructor_id char(5), raise_date date, raise_amt numeric(7,2));

declare
dept instructor.dept_name%TYPE := '&dept_name';
cur_date date; 
cursor c1 is select * from instructor for update;
begin
select current_date into cur_date from dual;
for i in c1
loop
if i.dept_name = dept then 
begin
update instructor set salary = salary * 1.05 where current of c1;
insert into salary_raise values(i.id, cur_date, i.salary / 21);
dbms_output.put_line(i.id);
end;
end if; 
end loop;
end;
/