declare
cursor c1 is select * from student natural left outer join takes where course_id = 'CS-101';
begin
for i in c1
loop
if i.tot_cred < 30 then
dbms_output.put_line('Deregistering ' || i.name || ' from CS-101');
delete from takes where id=i.id and course_id='CS-101';
end if;
end loop;
end;
/