set serveroutput on
create or replace trigger all_takes_trigger
before insert or update or delete on takes 
for each row
BEGIN 
    CASE 
        WHEN inserting then
        insert into log_change_takes(time_of_change,id,course_id,sec_id,semester,year,grade) VALUES (SYSTIMESTAMP,:new.ID,:new.course_id,:new.sec_id,:new.semester,:new.year,:new.grade);
        WHEN updating then
        insert into log_change_takes(time_of_change,id,course_id,sec_id,semester,year,grade) VALUES (SYSTIMESTAMP,:old.ID,:old.course_id,:old.sec_id,:old.semester,:old.year,:old.grade);
        WHEN deleting then
        insert into log_change_takes(time_of_change,id,course_id,sec_id,semester,year,grade) VALUES (SYSTIMESTAMP,:old.ID,:old.course_id,:old.sec_id,:old.semester,:old.year,:old.grade);
    END CASE;
END;
/