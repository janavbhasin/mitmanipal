set serveroutput on
create or replace function sqr(num number)
return number as
x number;
BEGIN
    x:=num*num;
    return x;
END;
/
BEGIN
    dbms_output.put_line(sqr(3));
END;
/