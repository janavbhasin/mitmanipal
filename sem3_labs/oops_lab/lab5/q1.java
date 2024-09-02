import java.util.*;
class EMPLOYEE 
{
    int eid;
    String ename,email;
    double ebasic,egross_Sal,enetsalary,eIT,eDA;
    EMPLOYEE(int id, String name, double basic) 
    {
        eid = id;
        ename = formatemployeename(name);
        ebasic = basic;
        email=generateemail(name);
    }
    String formatemployeename(String name)
    {
        StringBuilder result=new StringBuilder();
        String []words=name.split(" ");
        for (String word:words)
        {
            String str=word.toLowerCase();
            result.append(Character.toUpperCase(word.charAt(0))+str.substring(1));
            result.append(" ");
        }
        return result.toString();
    }
    String generateemail(String name)
    {
        StringBuilder result=new StringBuilder();
        String []words=name.split(" ");
        int i=1;
        for(String word :words)
        {
            if(i==1)
            {
                i=0;
                result.append(Character.toUpperCase(word.charAt(0)));
            }
            else
            {
                result.append(word.toLowerCase());
            }
        }
        result.append("@gmail.com");
        return result.toString();
    }
    void compute() 
    {
        eDA = 0.52 * ebasic;
        egross_Sal = ebasic + eDA;
        eIT = 0.30 * egross_Sal;
        enetsalary = egross_Sal - eIT;
    }
    void display() 
    {
        System.out.println("Employee name: " + ename+"\nEmployee id: "+eid+"\nNet salary: "+enetsalary+"\nemail:"+email);
    }
    void read() 
    {
        Scanner Sc = new Scanner(System.in);
        System.out.println("Enter the name of the employee: ");
        ename = Sc.nextLine();
        System.out.println("Enter the id of employee: ");
        eid = Sc.nextInt();
        System.out.println("Enter the basic salary of employee: ");
        ebasic = Sc.nextDouble();
    }
}
class q1
{
    public static void main(String args[]) 
    {
        System.out.println("Enter the number of employees: ");
        Scanner Sc = new Scanner(System.in);
        int n = Sc.nextInt();
        Sc.nextLine();
        EMPLOYEE[] ee = new EMPLOYEE[n];
        int i=0;
        for (i = 0; i < n; i++) 
        {
            System.out.println("Enter details for Employee " + (i + 1));
            System.out.println("Enter the name of the employee: ");
            String name = Sc.nextLine();
            System.out.println("Enter the id of employee: ");
            int id = Sc.nextInt();
            System.out.println("Enter the basic salary of employee: ");
            double basic = Sc.nextDouble();
            ee[i] = new EMPLOYEE(id, name, basic);
            ee[i].compute();
            Sc.nextLine();
        }
        for (i = 0; i < n; i++) 
        {
            ee[i].display();
        }
    }
}