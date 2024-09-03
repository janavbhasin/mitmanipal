set serveroutput on;
create or replace package q7 as
	procedure list_instructor(dname varchar2);
	function max_salary(xyz varchar2)
	return number;
end q7;
/
create or replace package body q7 as 
procedure list_instructor(dname varchar2) is
cursor insts is select name from instructor where dept_name=dname;
BEGIN
	for i in insts loop
		dbms_output.put_line(i.name);
	end loop;
END list_instructor;
function max_salary(xyz varchar2)
return number is
inst number;
BEGIN
	select max(salary) into inst from instructor where dept_name=xyz;
	return inst;
END max_salary;
END q7;
/
BEGIN
	dbms_output.put_line(q7.max_salary('Comp. Sci.'));
	q7.list_instructor('Comp. Sci.');
END;
/