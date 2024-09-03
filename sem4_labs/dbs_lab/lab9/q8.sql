set serveroutput on
create or replace procedure intrest(principle in number,rate in number,years in number,times in number,SI out numeric,CI out numeric,tot_sum in out numeric) as
BEGIN
    SI:=(principle*rate*years)/100;
    CI :=principle*power((1+rate/times),times*years);
	tot_sum := principle + SI + CI;
END;
/
DECLARE
    principle_val NUMBER := 1000;
    rate_val NUMBER := 0.05;
    years_val NUMBER := 5;
    times_val NUMBER := 12;
    SI_val NUMBER;
    CI_val NUMBER;
    tot_sum_val NUMBER;
BEGIN
    intrest(principle_val, rate_val, years_val, times_val, SI_val, CI_val, tot_sum_val);
    DBMS_OUTPUT.PUT_LINE('Simple Interest: ' || SI_val);
    DBMS_OUTPUT.PUT_LINE('Compound Interest: ' || CI_val);
    DBMS_OUTPUT.PUT_LINE('Total Amount: ' || tot_sum_val);
END;
/