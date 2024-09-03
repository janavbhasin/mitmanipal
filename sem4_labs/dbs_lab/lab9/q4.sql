set serveroutput on
	create or replace procedure naming(dname varchar2) is 
	cursor stud is (select name from student where dept_name=dname);
	cursor cursed is (select title from course where dept_name=dname);
BEGIN
	for i in stud loop
		dbms_output.put_line(i.name);
	end loop;
	for i in cursed loop
		dbms_output.put_line(i.title);
	end loop;
END;
/