import java.util.*;
class Student
{
    String sname;
    int array_marks[]=new int [5];
    int total=0;
    int average;
    void assign(int marks[],String name)
    {
        sname=name;
        for (int i=0;i<5;i++)
        {
            array_marks[i]=marks[i];
        }
    }
    void display()
    {
        System.out.println("name is: "+sname);
        for(int i=0;i<5;i++)
        {
            System.out.println(array_marks[i]);
        }
        System.out.println("average is: "+average);
        System.out.println("total is: "+total);
    }
    void compute()
    {
        for(int i=0;i<5;i++)
        {
            total=total+array_marks[i];
        }
        average=total/5;
    }
}
class Sciencestudent extends Student
{
    private int practicalmarks;
    void newassign(String name,int marks[],int practicalmarks)
    {
        super.assign(marks,name);
        this.practicalmarks=practicalmarks;
    }
    void compute()
    {
        int tot=0;
        for(int i=0;i<5;i++)
        {
            tot=tot+super.array_marks[i];
        }
        super.total=tot+practicalmarks;
        super.average=super.total/6;
    }
    void displaypracticalmarks()
    {
        System.out.println("practical marks are:"+practicalmarks);
    }
}
class Artsstudent extends Student
{
    String elective;
    void new2assign(int marks[],String name,String elective)
    {
        super.assign(marks,name);
        this.elective=elective;
    }
    String getelective()
    {
        return elective;
    }
}
class q1
{
    public static void main(String args[])
    {
        Scanner Sc=new Scanner(System.in);
        int marks[]=new int[5];
        System.out.println("enter name:");
        String name=Sc.next();
        System.out.println("enter marks:");
        for(int i=0;i<5;i++)
        {
            marks[i]=Sc.nextInt();
        }

        Student st=new Student();
        st.assign(marks,name);
        st.compute();
        st.display();

        Sciencestudent sct=new Sciencestudent();
        sct.newassign(name,marks,12);
        sct.compute();
        sct.display();
        sct.displaypracticalmarks();

        Artsstudent art=new Artsstudent();
        art.new2assign(marks,name,"polscience");
        art.compute();
        art.display();
        String ele=art.getelective();
        System.out.println("elective is :"+ele);
    }
}