set serveroutput on
DECLARE
    names instructor.name%type;
    ids instructor.id%type;
    dept instructor.dept_name%type;
    sal instructor.salary%type;
BEGIN
    select name ,id,dept_name ,salary into names,ids,dept,sal from instructor where name ='&name';
    dbms_output.put_line('details are :');
    dbms_output.put_line('id: '||ids||' name: '||names||' department name: '||dept||' salary: '||sal);
    exception
    when no_data_found then dbms_output.put_line('no instructor found');
    when dup_val_on_index then dbms_output.put_line('multiple user found');
    when too_many_rows then dbms_output.put_line('too may rows found');
END;
/