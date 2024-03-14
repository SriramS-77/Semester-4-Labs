declare
course varchar(20) := '&course';
cursor c1 is select distinct id, name from instructor natural full outer join teaches where course_id=course;
begin
for i in c1
loop
dbms_output.put_line('ID = ' || i.id || ', Name = ' || i.name);
end loop;
end;
/