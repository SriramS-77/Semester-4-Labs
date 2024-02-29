declare
cursor c1 is select * from student order by tot_cred;
a numeric(2) := 0;
id student.id%TYPE;
name student.name%TYPE;
dept student.dept_name%TYPE;
credits student.tot_cred%TYPE;
begin
while a < 10
loop
fetch next from c1 into id, name, dept, credits;
dbms_output.put_line('ID = ' || id || ', Name = ' || name || ', Dept = ' || dept || ', Credits = ' || credits);
a := a + 1;
exit when c1%NOTFOUND;
end loop;
end;
/

declare
cursor c1 is select * from student order by tot_cred;
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
