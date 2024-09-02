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
    synchronized void produce (int item)throws InterruptedException
    {
        while(full)
        {
            wait();
        }
        buffer=item;
        System.out.println("produced"+item);
        full=true;
        notify();
    }
    synchronized void consumer(int item)throws InterruptedException
    {
        while(!full)
        {
            wait();
        }
        buffer =item;
        System.out.println("consumed"+buffer);
        full=false;
        notify();
    }
}
class producer implements Runnable
{
    private sharedbuffer buff;
    public producer(sharedbuffer x)
    {
        buff=x;
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
class consumer implements Runnable
{
    public  sharedbuffer buff;
    public consumer(sharedbuffer buf)
    {
        buff=buf;
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
class q3
{
    public static void main(String args[])
    {
        sharedbuffer buffer = new sharedbuffer();
        Thread producerThread = new Thread(new producer(buffer));
        Thread consumerThread = new Thread(new consumer(buffer));

        producerThread.start();
        consumerThread.start();
    }
}