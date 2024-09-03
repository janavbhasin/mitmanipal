set serveroutput on
DECLARE 
    cursor c is select * from teaches;
    n number;
    courseRow course%ROWTYPE;
    iname instructor.name%TYPE;
    sectionRow section%ROWTYPE;
BEGIN
    for i in c
    loop
        BEGIN
            select  count(*) into n from takes group by course_id,sec_id,semester,year having  course_id=i.course_id and semester=i.semester and year=i.year and sec_id=i.sec_id;
            exception
                when no_data_found then n:=0;
            end;
            select name into iname from instructor where i.id=id;
            select * into sectionRow from section where sec_id=i.sec_id and course_id=i.course_id and semester=i.semester and year=i.year;
            select * into courseRow from course where course_id=i.course_id;
            DBMS_OUTPUT.PUT_LINE('Course ID: ' || I.course_id || ' Title: ' || courseRow.title || ' Dept name: ' || courseRow.dept_name || ' Credits: ' || courseRow.credits || 
        ' Instructor name: ' || iname || ' Building: ' || sectionRow.building || ' Room number: ' || sectionRow.room_number || ' Time slot id: ' || sectionRow.time_slot_id || ' Total students enrolled: ' || n);
    end loop;
end;
/