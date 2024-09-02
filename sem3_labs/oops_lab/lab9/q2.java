import java.util.*;
class Matrix implements Runnable
{
    int arr[];
    int rsum,a;
    int totalsumarray[];
    Matrix(int art[],int at[],int i)
    {
        a=i;
        arr=art;
        totalsumarray=at;
    }
    public void run()
    {
        for(int ar:arr)
        {
            rsum+=ar;
        }
        synchronized(totalsumarray) 
        {
            totalsumarray[0]+=rsum;
        }
        System.out.println("ros sum of"+(a+1)+"is"+rsum);
    }
}
class q2
{
   public static void main(String args[])
   {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the order of the matrix");
        int m=sc.nextInt();
        int n=sc.nextInt();
        int arr[][]=new int[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                arr[i][j]=sc.nextInt();
            }
        }
        Matrix mt[]=new Matrix[m];
        int totalsumarray[]=new int[1];
        totalsumarray[0]=0;
        for(int i=0;i<m;i++)
        {
            mt[i]=new Matrix(arr[i],totalsumarray,i);
            try
            {
                Thread.sleep(1000);
            }catch(InterruptedException e){}
        }
        Thread th[]=new Thread[m];
        for(int i=0;i<m;i++)
        {
            th[i]=new Thread(mt[i]);
            th[i].start();
            try
            {
                th[i].join();
            }catch(InterruptedException exp){}
        }
        System.out.println("total is"+totalsumarray[0]);
   }
}