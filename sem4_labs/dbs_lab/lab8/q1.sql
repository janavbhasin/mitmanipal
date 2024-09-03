create table salary_raise(
    instructor_id number,
    raise_date date,
    raise_amt number);
DECLARE
    str instructor.dept_name%TYPE;
    CURSOR c IS 
        SELECT * FROM instructor WHERE dept_name = str FOR UPDATE OF salary;
BEGIN
    str := '&Department name';
    FOR inst IN c LOOP
        UPDATE instructor 
        SET salary = salary * 1.05
        WHERE CURRENT OF c;
        
        INSERT INTO salary_raise (instructor_id, raise_date, raise_amt) 
        VALUES (inst.id, SYSDATE, inst.salary * 0.05);
        Commit;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Salary raises successfully applied.');
END;
/