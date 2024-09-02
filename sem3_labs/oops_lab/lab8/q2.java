import java.util.*;
class MyExceptions extends Exception
{
    private String err;
    MyExceptions(String err)
    {
        this.err=err;
    }
    String getcode()
    {
        return err;
    }
}
class Currentdate
{
    int date,month,year;
    void createdate()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter day ");
        date = sc.nextInt();
        System.out.println("Enter month ");
        month = sc.nextInt();
        System.out.println("Enter year ");
        year = sc.nextInt();
    }
}
class q2
{
    public static void main(String args[])
    {
        MyExceptions invalMonth=new MyExceptions("invalid month");
        MyExceptions invalDay=new MyExceptions("invalid date");
        Currentdate cd= new Currentdate();
        try
        {
            cd.createdate();
            if(cd.month>12||cd.month<1)
            {
                throw invalMonth;
            }
            else if(cd.month%2==1)
            {
                if(cd.date>31||cd.date<1)
                {
                    throw invalDay;
                }
            }
            else if(cd.month%2==0)
            {
                if(cd.month==2)
                {
                    if(cd.year%4==0)
                    {
                        if(cd.date>29 || cd.date<1)
                        {
                            throw invalDay;
                        }
                    }
                    else if (cd.date>28 || cd.date<1)
                    {
                        throw invalDay;
                    }
                }
                else if(cd.date>30||cd.date<1)
                {
                    throw invalDay;
                }
            }
            System.out.println(cd.date+"/"+cd.month+"/"+cd.year);
        }
        catch(MyExceptions exp)
        {
            System.out.println(exp.getcode());
        }
    }
}