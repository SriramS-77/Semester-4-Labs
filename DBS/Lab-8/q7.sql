declare
cursor c1 is select distinct s_id, name from (select * from teaches te left outer join advisor ad on te.id=ad.i_id) a natural inner join (select id as s_id, name, course_id, sec_id, semester, year from takes natural inner join student);    
begin
for i in c1
loop
dbms_output.put_line('Student ' || i.name || ' registered to a course taught by his advisor');
end loop;
end;
/