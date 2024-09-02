import java.util.*;
class complex
{
    int r,i;
    complex(int a,int b)
    {
        r = a;
        i = b;
    }
    void display()
    {
        System.out.println(r+"+"+i+"i");
    }
}
class swapper
{
    int x,y;
    swapper(int x,int y)
    {
        this.x=x;
        this.y=y;
    }
    int getx()
    {
        return x;
    }
    int gety()
    {
        return y;
    }
    void swap()
    {
        int a=x;
        x=y;
        y=a;
    }
}
class p1
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the complex number values");
        int a=sc.nextInt();
        int b=sc.nextInt();
        complex comp = new complex(a,b);
        comp.display();
        System.out.println("enter values of x and y");
        int x=sc.nextInt();
        int y=sc.nextInt();
        swapper sw = new swapper(x,y);
        int i=0;
        while(i!=4)
        {
            System.out.println("1 for get x\n2 for get y\n3 for swap\n4 for exit\n");
            i=sc.nextInt();
            if(i==1)
            {
                System.out.println("\nx is "+sw.getx());
            }
            else if(i==2)
            {
                System.out.println("\ny is "+sw.gety());
            }
            else if(i==3)
            {
                sw.swap();
            }
            else if(i==4)
            {
                System.out.println("bye bye\n");
            }
        }
    }
}