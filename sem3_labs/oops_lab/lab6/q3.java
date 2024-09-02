import java.util.*;
class Person
{
    private String name;
    private String dob;
    Person(String n,String d)
    {
        name=n;
        dob=d;
    }
    String getname()
    {
        return name;
    }
    String getdob()
    {
        return dob;
    }
}
class Collegegraduate extends Person
{
    private int year;
    private float gpa;
    Collegegraduate(String n,String d,int y,float g)
    {
        super(n,d);
        gpa=g;
        year=y;
    }
    int getyear()
    {
        return year;
    }
    float getgpa()
    {
        return gpa;
    }
}
class q3
{
    public static void main(String args[])
    {
        String name,dob;
        int year;
        float gpa;
        Scanner Sc=new Scanner(System.in);
        System.out.println("enter the name:");
        name=Sc.next();
        System.out.println("enter the date of birth(dd/mm/yyyy):");
        dob=Sc.next();
        System.out.println("enter the gpa:");
        gpa=Sc.nextFloat();
        System.out.println("enter the year of graduation:");
        year=Sc.nextInt();
        Collegegraduate cg=new Collegegraduate(name,dob,year,gpa);
        System.out.println("name is:"+cg.getname());
        System.out.println("dob is:"+cg.getdob());
        System.out.println("gpa is:"+cg.getgpa());
        System.out.println("year of graduation is:"+cg.getyear());
    }
}