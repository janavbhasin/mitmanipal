set serveroutput on
create or replace trigger inst_sal
before update of salary on instructor
for each row 
BEGIN
    insert into old_data_instructor(id,name,dept_name,salary) values(:old.id,:old.name,:old.dept_name,:old.salary);
END;
/