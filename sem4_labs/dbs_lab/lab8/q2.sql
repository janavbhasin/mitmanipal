set serveroutput on
DECLARE 
    cursor c is SELECT * from(select * from  student order by tot_cred) where rownum<11;
BEGIN
    for i in c
    LOOP  
        DBMS_OUTPUT.PUT_LINE('ID: ' || i.id || ' Name: ' || i.name || ' Dept_name: ' || i.dept_name || ' Total credits: ' || i.tot_cred);
    end loop;
end;
/