import java.util.*;
class Building
{
    int sqf;
    int stories;
    void set1(int sqf,int stories)
    {
        this.sqf=sqf;
        this.stories=stories;
    }
    int sqf()
    {
        return sqf;
    }
    int stories()
    {
        return stories;
    }
}
class House extends Building
{
    int bed;
    int bath;
    void set2(int sqf,int stories,int bed,int bath)
    {
        super.set1(sqf,stories);
        this.bed=bed;
        this.bath=bath;
    }
    int bed()
    {
        return bed;
    }
    int bath()
    {
        return bath;
    }
}
class School extends Building
{
    int clas;
    String grade;
    void set3(int sqf,int stories,int clas,String grade)
    {
        super.set1(sqf,stories);
        this.clas=clas;
        this.grade=grade;
    }
    int clas()
    {
        return clas;
    }
    String grade()
    {
        return grade;
    }
}
class q4 
{
    public static void main(String args[])
    {
        System.out.println("enter 1 for house and 2 for school");
        Scanner Sc=new Scanner(System.in);
        int a=Sc.nextInt();
        Sc.nextLine();
        if(a==1)
        {
            School sc=new School();
            System.out.println("enter sqf,stories,class,grade");
            int sqf=Sc.nextInt();
            int stories=Sc.nextInt();
            int clas=Sc.nextInt();
            String grade=Sc.next();
            sc.set3(sqf,stories,clas,grade);
            System.out.println("sqf: " + sc.sqf());
            System.out.println("stories: " + sc.stories());
            System.out.println("class: " + sc.clas());
            System.out.println("grade: " + sc.grade());
        }
        else if (a==2)
        {
            House hs=new House();
            System.out.println("enter sqf,stories,bed,bath");
            int sqf=Sc.nextInt();
            int stories=Sc.nextInt();
            int bed=Sc.nextInt();
            int bath=Sc.nextInt();
            hs.set2(sqf,stories,bed,bath);
            System.out.println("sqf: " + hs.sqf());
            System.out.println("stories: " + hs.stories());
            System.out.println("bed: " + hs.bed());
            System.out.println("bath: " + hs.bath());
        }
    }
}