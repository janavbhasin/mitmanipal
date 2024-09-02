import java.util.*;
class StackDemo<T> 
{
    List<T> st;
    int tos, size;
    StackDemo(int n) 
    {
        tos = -1;
        st = new ArrayList<T>(n);
        size = n;
    }
    void push(T x) 
    {
        if (tos == (size - 1)) 
        {
            System.out.println("Stack full");
            return;
        }
        st.add(++tos, x);
    }
    T pop() 
    {
        if (tos < 0) 
        {
            System.out.println("Stack is empty");
            return null;
        }
        return st.remove(tos--);
    }
}
class Student 
{
    String name;
    int rollNumber;
    Student(String name, int rollNumber) 
    {
        this.name = name;
        this.rollNumber = rollNumber;
    }
}
class Employee 
{
    String name;
    int employeeId;
    Employee(String name, int employeeId) 
    {
        this.name = name;
        this.employeeId = employeeId;
    }
}
class q3 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the stack");
        int n = sc.nextInt();
        StackDemo<Student> studentStack = new StackDemo<>(n);
        StackDemo<Employee> employeeStack = new StackDemo<>(n);
        System.out.println("1. Push Student\n2. Pop Student\n3. Push Employee\n4. Pop Employee\n5. Exit");
        int choice;
        do 
        {
            System.out.println("Enter your choice");
            choice = sc.nextInt();
            if (choice == 1) 
            {
                System.out.println("Enter name ");
                String name = sc.next();
                System.out.println("Enter roll number ");
                Student student = new Student(name, sc.nextInt());
                studentStack.push(student);
            } 
            else if (choice == 2) 
            {
                Student student = studentStack.pop();
                if (student != null) 
                {
                    System.out.println("\nPopped contents:\nName: " + student.name + "\tRoll no: " + student.rollNumber + "\n");
                }
            } 
            else if (choice == 3) 
            {
                System.out.println("Enter name ");
                String name = sc.next();
                System.out.println("Enter employee ID ");
                Employee employee = new Employee(name, sc.nextInt());
                employeeStack.push(employee);
            } 
            else if (choice == 4) 
            {
                Employee employee = employeeStack.pop();
                if (employee != null) 
                {
                    System.out.println("\nPopped contents:\nName: " + employee.name + "\tID: " + employee.employeeId + "\n");
                }
            }
        } while (choice != 5);
        System.out.println("bye bye");
    }
}