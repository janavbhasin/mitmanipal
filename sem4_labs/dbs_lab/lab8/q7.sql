set serveroutput on
DECLARE
    cursor c1 is select * from advisor;
    cursor c2(i takes.id%TYPE) is select * from takes where id=i;
    cursor c3(i teaches.id%TYPE) is select * from teaches where id=i;
    stdname student.name%TYPE;
    flag numeric(1):=0;
BEGIN
    for i in c1
    loop
        for j in c2(i.s_id)
        loop
            for z in c3(i.i_id)
            loop
            if j.course_id=z.course_id and j.sec_id=z.sec_id and j.semester=z.semester and j.year=z.year then
                select name into stdname from student where id=j.id;
                dbms_output.put_line('ID: ' || j.id || 'Name: ' || stdName);
                flag:=1;
            end if;
            end loop;
        if flag =1 then exit;
        end if;
        end loop;
    end loop;
end;
/