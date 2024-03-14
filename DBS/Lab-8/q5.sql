create table student_table (rollno numeric(2), gpa numeric(3, 2));
insert into student_table values(1, 5.8);
insert into student_table values(2, 6.5);
insert into student_table values(3, 3.4);
insert into student_table values(4, 7.8);
insert into student_table values(5, 9.5);

alter table student_table add (grade char(2));

update student_table set grade = 'F'; 

declare
lgrade char(2);
cursor c1 is select * from student_table for update;
begin
for i in c1
loop
if i.gpa > 9 then lgrade := 'A+';
elsif i.gpa > 8 then lgrade := 'A';
elsif i.gpa > 7 then lgrade := 'B';
elsif i.gpa > 6 then lgrade := 'C';
elsif i.gpa > 5 then lgrade := 'D';
elsif i.gpa > 4 then lgrade := 'E';
else lgrade := 'F';
end if;
update student_table set grade = lgrade where current of c1;
end loop;
end;
/
