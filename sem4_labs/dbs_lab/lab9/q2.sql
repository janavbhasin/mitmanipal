set serveroutput on
create or replace procedure dept_inst_course(dname varchar2) is 
cursor inst is select name from instructor where dept_name=dname;
cursor depts is select title from course where dept_name=dname;
BEGIN
	dbms_output.put_line('Instructors: ');
	for i in inst
	loop
		dbms_output.put_line(i.name);
	end loop;
	dbms_output.put_line('Departments:');
	for i in depts 
	loop
		dbms_output.put_line(i.title);
	end loop;
end;
/
BEGIN
	dept_inst_course('Comp. Sci.');
end;
/