set serveroutput on
DECLARE
    g studenttable.gpa%TYPE;
    maxg studenttable.gpa%TYPE;
    n numeric(2);
    i numeric(2);
    maxroll studenttable.rollno%TYPE;
BEGIN
    select count(*) into n from studenttable ;
    maxg:=0;
    for i in 1..n loop
        select gpa into g from studenttable where rollno=i;
        if g>maxg then
            maxg:=g;
            maxroll:=i;
        end if;
    end loop;
    dbms_output.put_line('the student with max gpa of '||maxg||' is roll no '||maxroll);
END;
/    