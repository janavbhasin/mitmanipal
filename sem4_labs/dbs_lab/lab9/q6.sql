set serveroutput on
create or replace function department_highest(dname varchar2) 
return number as
inst number;
BEGIN
	select max(salary) into inst from instructor where dept_name =dname;
	return inst;
END;
/
BEGIN
	dbms_output.put_line(department_highest('Comp. Sci.'));
END;
/