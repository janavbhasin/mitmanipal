set serveroutput on
DECLARE
    i numeric(2);
    g studenttable.gpa%type;
    a varchar(10);
BEGIN
    i:=1;
    loop 
        select gpa into g from studenttable where rollno=i;
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
        dbms_output.put_line('grade is :'||a);
        i:=i+1;
        if i>5 then exit;
        end if;
    end loop;
end;
/