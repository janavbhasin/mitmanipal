set serveroutput on 
DECLARE
    cursor c(cid teaches.course_id%TYPE) is select distinct id from teaches where course_id =cid;
    iname instructor.name%TYPE;
    cid teaches.course_id%TYPE;
BEGIN
    cid:='&course_id';
    for i in c(cid) 
    loop
        select name into iname from instructor where i.id=id;
        dbms_output.put_line('ID: ' || i.id || ' Name: ' || iname);
    end loop;
end;
/