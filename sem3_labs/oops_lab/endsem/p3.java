import java.util.*;
class sharedbuffer
{
    int buffer;
    boolean full;
    sharedbuffer()
    {
        buffer=0;
        full=false;
    }
    synchronized void produce(int item)throws InterruptedException
    {
        while(full)
        {
            wait();
        }
        buffer=item;
        System.out.println("produced :"+item);
        full=true;
        notify();
    }
    synchronized void consumer(int item)throws InterruptedException
    {
        while(!full)
        {
            wait();
        }
        buffer=item;
        System.out.println("consumed :"+item);
        full=false;
        notify();
    }
}
class produce implements Runnable
{
    private sharedbuffer buff;
    public produce(sharedbuffer buff)
    {
        this.buff=buff;
    }
    public void run()
    {
        for(int i=0;i<5;i++)
        {
            try
            {
                buff.produce(i);
            }catch(InterruptedException e){}
        }
    }
}
class consumed implements Runnable
{
    private sharedbuffer buff;
    public consumed(sharedbuffer buff)
    {
        this.buff=buff;
    }
    public void run()
    {
        for(int i=0;i<5;i++)
        {
            try
            {
                buff.consumer(i);
            }catch(InterruptedException e){}
        }
    }
}
class p3
{
    public static void main(String args[])
    {
        sharedbuffer buff = new sharedbuffer();
        Thread producerThread=new Thread(new produce(buff));
        Thread consumerThread=new Thread(new consumed(buff));

        producerThread.start();
        consumerThread.start();
    }
}