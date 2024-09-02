import java.util.*;
class MyException extends Exception
{
    private String err;
    MyException()
    {
        err="seats filled";
    }
    String getcode()
    {
        return err;
    }
}
class Student
{
    int roll;
    String name;
    static int count=0;
    int reg;
    Student()throws MyException
    {
        count++;
        if(count>=3)
        {
            throw new MyException();
        }
    }
    void assign()
    {
        Scanner Sc=new Scanner(System.in);
        System.out.println("enter roll:");
        roll=Sc.nextInt();
        System.out.println("enter name:");
        name=Sc.next();
        reg=createroll(roll);
    }
    int createroll(int a)
    {
        int x=a*100;
        reg=x+count;
        return reg;
    }
    void display()
    {
        System.out.println("roll is:"+roll);
        System.out.println("name is:"+name);
        System.out.println("reg is:"+reg);
    }
}
class q3
{
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        System.out.println("enter number of students");
        int n=sc.nextInt();
        Student st[]=new Student[n];
        for(int i=0;i<n;i++)
        {
            try
            {
                st[i]=new Student();
                st[i].assign();
            }
            catch(MyException e)
            {
                System.out.println(e.getcode());
            }
        }
        for(int i=0;i<n;i++)
        {
            st[i].display();
        }
    }
}