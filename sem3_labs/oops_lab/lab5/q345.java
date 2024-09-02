import java.util.*;
class Student 
{
    int regno;
    String name;
    GregorianCalendar doj;
    short sem;
    float gpa, cgpa;
    static int count = 1;
    Student(String nam, int d, int m, int y, short semester, float g, float cg) 
    {
        GregorianCalendar greg = new GregorianCalendar(y, m, d);
        String regst = String.format("%02d%d", count++, y % 100);
        regno = Integer.parseInt(regst);
        name = nam.replaceAll("\\b\\w", "$0. ");
        doj = greg;
        sem = semester;
        gpa = g;
        cgpa = cg;
    }
    void display() 
    {
        System.out.printf("Name: %s\nRegistration No: %d\nDate of Joining: %d/%d/%d\nSemester: %d\nGPA: %.2f\nCGPA: %.2f\n",
        name, regno, doj.get(Calendar.DAY_OF_MONTH), doj.get(Calendar.MONTH) + 1, doj.get(Calendar.YEAR), sem, gpa, cgpa);
    }
    static void sortByName(Student[] students) 
    {
        Arrays.sort(students, Comparator.comparing(student -> student.name));
    }
    static void sortBySemAndCGPA(Student[] students) 
    {
        Arrays.sort(students, (s1, s2) -> {
            if (s1.sem != s2.sem) return Integer.compare(s2.sem, s1.sem);
            return Float.compare(s2.cgpa, s1.cgpa);
        });
    }
}
public class q345 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of students (Minimum 5): ");
        int n = sc.nextInt();
        sc.nextLine();
        Student[] students = new Student[n];
        for (int i = 0; i < n; i++) 
        {
            System.out.println("\nEnter details for student number " + (i + 1));
            System.out.print("Enter your name: ");
            String name = sc.nextLine();
            System.out.print("Enter day of DOJ: ");
            int day = sc.nextInt();
            System.out.print("Enter month of DOJ: ");
            int month = sc.nextInt();
            System.out.print("Enter year of DOJ: ");
            int year = sc.nextInt();
            System.out.print("Enter your semester: ");
            short semester = sc.nextShort();
            System.out.print("Enter your gpa: ");
            float gpa = sc.nextFloat();
            System.out.print("Enter your cgpa: ");
            float cgpa = sc.nextFloat();
            sc.nextLine();
            students[i] = new Student(name, day, month, year, semester, gpa, cgpa);
        }
        System.out.println("\nDetails of all students:\n");
        for (int i = 0; i < n; i++) 
        {
            System.out.println("\nDetails for student number " + (i + 1));
            students[i].display();
        }
        System.out.print("Enter a character: ");
        char ch = sc.next().charAt(0);
        System.out.println("The students with their name starting with the character are: ");
        for (Student student : students) 
        {
            if (student.name.charAt(0) == ch) 
            {
                student.display();
            }
        }
        System.out.println("1. Sort by Sem and CGPA\n2. Sort by name\n3. Exit");
        int input = sc.nextInt();
        if (input == 1) 
        {
            Student.sortBySemAndCGPA(students);
            System.out.println("Students sorted by sem and cgpa:\n");
        } else if (input == 2) 
        {
            Student.sortByName(students);
            System.out.println("Students sorted by name:\n");
        } else 
        {
            System.out.println("Bye Bye");
            sc.close();
            return;
        }
        for (Student student : students) 
        {
            student.display();
        }
        sc.close();
    }
}