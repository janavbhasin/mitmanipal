import java.util.Scanner;
interface Series
{
    int getnext();
    void reset();
    void setstart(int x);
}
class Bytwos implements Series
{
    int a,nex;
    public int getnext()
    {
        nex=nex+2;
        return nex;
    }
    public void reset()
    {
        nex=a;
    }
    public void setstart(int x)
    {
        a=x;
        nex=x;
    }
}
class q3
{
    public static void main(String args[])
    {
        Scanner Sc = new Scanner(System.in);
        int ch=0;
        Bytwos bt= new Bytwos();
        while(ch!=4)
        {
            System.out.println("\nenter\n1 for set\n2 for reset\n3 for get next\n4 for exit");
            ch=Sc.nextInt();
            if(ch==1)
            {
                int x;
                System.out.println("enter value");
                x=Sc.nextInt();
                bt.setstart(x);
            }
            else if(ch==2)
            {
                bt.reset();
            }
            else if(ch==3)
            {
                System.out.println(bt.getnext());
            }
            else if(ch==4)
            {
                System.out.println("bye bye");
            }
        }
    }
}