set serveroutput on
DECLARE 
    cursor c is select * from takes where course_id='CS-101';
    tot number;
BEGIN
for i in c 
    loop
    select tot_cred into tot from student where i.id=student.id;
    if tot<50 then
        delete from takes where course_id=i.course_id and id=i.id and i.sec_id=sec_id and i.semester=semester;
    end if;
    end loop;
end;
/