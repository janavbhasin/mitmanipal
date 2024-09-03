set serveroutput on
DECLARE
    rno studenttable.rollno%type;
    g studenttable.gpa%type;
BEGIN
    rno:='&rno';
    select gpa into g from studenttable where rollno=rno;
    dbms_output.put_line('Gpa: '||g);
END;
/