import java.util.Scanner;
abstract class figure 
{
    int a, b;
    abstract int area();
    abstract int perimeter();
}
class Rectangle extends figure 
{
    Rectangle(int x, int y) 
    {
        a = x;
        b = y;
    }
    int area() 
    {
        return (a * b);
    }
    int perimeter()
    {
        return 2*(a+b);
    }
}
class Square extends figure 
{
    Square(int x) 
    {
        a = x;
    }
    int area() 
    {
        return (a * a);
    }
    int perimeter()
    {
        return 4*a;
    }
}
class Triangle extends figure 
{
    Triangle(int x, int y) 
    {
        a = x;
        b = y;
    }
    int area() 
    {
        return ((int) a * b / 2);
    }
    int perimeter()
    {
        return (3*(a+b))/2;
    }
}
public class q5
{
    public static void main(String args[]) 
    {
        Scanner sc = new Scanner(System.in);
        int area = 0, a, b,pe;
        System.out.println("rectangle ");
        a = sc.nextInt();
        b = sc.nextInt();
        Rectangle r = new Rectangle(a, b);
        area = r.area();
        pe=r.perimeter();
        System.out.println("The area is: " + area+"\nthe perimeter is"+pe);
        System.out.println("square ");
        a = sc.nextInt();
        Square sq = new Square(a);
        area = sq.area();
        pe=sq.perimeter();
        System.out.println("The area is: " + area+"\nthe perimeter is "+pe);
        System.out.println("triangle ");
        a = sc.nextInt();
        b = sc.nextInt();
        Triangle t = new Triangle(a, b);
        area = t.area();
        pe=t.perimeter();
        System.out.println("The area is: " + area+"\nthe perimeter is"+pe);
    }
}