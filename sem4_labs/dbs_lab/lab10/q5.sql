-- Step 1: Create the Advisor_Student view
CREATE VIEW Advisor_Student AS
SELECT *
FROM Advisor
NATURAL JOIN Student
NATURAL JOIN Instructor;

-- Step 2: Create the INSTEAD OF trigger
CREATE OR REPLACE TRIGGER delete_advisor_student
INSTEAD OF DELETE ON Advisor_Student
FOR EACH ROW
BEGIN
    DELETE FROM Advisor_Student
    WHERE advisor_id = :OLD.advisor_id
    AND student_id = :OLD.student_id
    AND instructor_id = :OLD.instructor_id;
END;
/
