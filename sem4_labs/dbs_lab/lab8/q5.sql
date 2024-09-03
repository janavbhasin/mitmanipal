set serveroutput on
DECLARE
    cursor c is select * from studenttable for update;
    g studenttable.gpa%TYPE;
    a studenttable.lettergrade%TYPE;
BEGIN
    for i in c
    loop
        g:=i.gpa;
        if g>0 and g<=4 then
		    a:='F';
        elsif g>4 and g<=5 then
            a:='E';
        elsif g>5 and g<=6 then
            a:='D';
        elsif g>6 and g<=7 then
            a:='C';
        elsif g>7 and g<=8 then
            a:='B';
        elsif g>8 and g<=9 then
            a:='A';
        elsif g>9 and g<=10 then
            a:='A+';
        else 
            a:='invalid';
        end if;
        update studenttable set lettergrade=a where current of c;
    end loop;
end;
/