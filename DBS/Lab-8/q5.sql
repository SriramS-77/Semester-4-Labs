declare
course_name varchar(20) := '&course';
cursor c1 is select * from instructor natural right outer join (select title, course_id from teaches natural full outer join where ;
a numeric(2) := 0;
begin
for i in c1
loop
dbms_output.put_line('ID = ' || i.id || ', Name = ' || i.name || ', Dept = ' || i.dept_name || ', Credits = ' || i.tot_cred);
a := a + 1;
exit when a=10;
end loop;
end;
/