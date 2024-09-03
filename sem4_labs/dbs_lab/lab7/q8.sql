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
            goto disp;
        elsif g>4 and g<=5 then
            a:='E';
            goto disp;
        elsif g>5 and g<=6 then
            a:='D';
            goto disp;
        elsif g>6 and g<=7 then
            a:='C';
            goto disp;
        elsif g>7 and g<=8 then
            a:='B';
            goto disp;
        elsif g>8 and g<=9 then
            a:='A';
            goto disp;
        elsif g>9 and g<=10 then
            a:='A+';
            goto disp;
        else 
            a:='invalid';
            goto disp;
        end if;
        <<disp>>
            dbms_output.put_line('grade is :'||a);
        i:=i+1;
        if i>5 then exit;
        end if;
    end loop;
end;
/