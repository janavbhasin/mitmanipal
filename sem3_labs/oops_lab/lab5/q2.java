import java.util.*;
import java.io.*;
class Student
{
    String name="";
    String new_name="";
    void extractInitials()
    {
        String words[]=name.split(" ");
        System.out.println("the initials are:");
        for(String word:words)
        {
            System.out.print(word.charAt(0));
            new_name=new_name+word;
        }
    }
    void removewhitespace()
    {
        System.out.println("\n"+new_name);     
        System.out.println("");   
    }
    void assign(String k)
    {
        name=k;
    }
    static String[] stringchange(String students[],int num)
    {
        int k=0;
        String arr[]=new String[num];
        for (int i=0;i<num;i++)
        {
            if (students[i].contains("bhasin"))
            {
                arr[k]=students[i];
                k=k+1;
            }
        }
        return Arrays.copyOf(arr, k);
    }
    static void sort(String students[],int num) 
    {
        for (int i=0;i<num;i++)
        {
            for (int j=i+1;j<num;j++)
            {
                if (students[i].compareTo(students[j]) > 0)
                {
                    String temp=students[i];
                    students[i]=students[j];
                    students[j]=temp;
                }
            }
        }
    }
}
class q2
{
    public static void main(String args[])
    {
        System.out.println("enter the number of students:");
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        sc.nextLine();
        Student[]st=new Student[n];
        String []names=new String[n];
        for(int i=0;i<n;i++)
        {
            st[i]=new Student();
            System.out.println("Enter the name:");
            String as=sc.nextLine();
            st[i].assign(as);
            names[i]=as;
        }
        for(int i=0;i<n;i++)
        {
            st[i].extractInitials();
            st[i].removewhitespace();
        }
        Student str =new Student();
        str.sort(names,n);
        for(int i=0;i<n;i++)
        {
            System.out.println(names[i]);
        }
        String[] studentsWithSubstring = str.stringchange(names, n);
        System.out.println("Students with the same substring 'bhasin' are:\n" + Arrays.toString(studentsWithSubstring));
    }
}