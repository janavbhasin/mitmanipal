import java.util.*;
class Mul implements Runnable
{
    int val;
    Mul(int x)
    {
        val=x;
    }
    public void run()
    {
        for(int i=0;i<11;i++)
        {
            System.out.println(val+"x"+i+"="+val*i+"\n");
        }
    }
}
class q1
{
    public static void main(String args[])
    {
        Mul ob1=new Mul(5);
        Mul ob2=new Mul(7);
        Mul ob3=new Mul(9);
        Thread th1=new Thread(ob1);
        Thread th2=new Thread(ob2);
        Thread th3=new Thread(ob3);
        th1.start();
        try
        {
            Thread.sleep(1000);
        }
        catch(InterruptedException e){}
        th2.start();
        try
        {
            Thread.sleep(1000);
        }
        catch(InterruptedException e){}
        th3.start();
        try
        {
            Thread.sleep(1000);
        }
        catch(InterruptedException e){}
    }
}