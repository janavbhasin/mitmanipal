set serveroutput on
	create or replace procedure course_popular(dname varchar2)is 
	mm number :=0;
	cid course.course_id%TYPE;
	cursor c is select course_id ,count(course_id) cc from takes natural join course group by course_id,dept_name having dept_name=dname;
BEGIN
	for i in c loop 
	if i.cc>mm then
		mm:=i.cc;
		cid:=i.course_id;
	end if;
	end loop;
	dbms_output.put_line('Most Popular Course is '||cid);
END;
/
BEGIN
	course_popular('Comp. Sci.');
END;
/