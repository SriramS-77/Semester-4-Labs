declare
cursor c1 is select * from (select * from (select course_id, title, dept_name, credits, count(id) as stu_count from course natural left outer join takes group by course_id, title, dept_name, credits) a natural left outer join section) b natural left outer join (select name, course_id, sec_id, semester, year from instructor natural full outer join teaches) c;
begin
for i in c1
loop
dbms_output.put_line('CourseID = ' || i.course_id || ', SecID = ' || i.sec_id || ', Dept = ' || i.dept_name || ', Title = ' || i.title || ', Semester = ' || i.semester || ', Year = ' || i.year || ', Credits = ' || i.credits || ', Building = ' || i.building || ', TimeSlot = ' || i.time_slot_id || ', Name of Instructor = ' || i.name || ', Enroll Count = ' || i.stu_count);
dbms_output.put_line('*******************************');
end loop;
end;
/