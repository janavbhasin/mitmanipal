import java.util.*;
class Stack
{
    int top;
    int arr[]=new int[5];
    Stack()
    {
        top=-1;
    }
    void push(int x)
    {
        try
        {
            top++;
            arr[top]=x;
        }
        catch(ArrayIndexOutOfBoundsException exp)
        {
            System.out.println("stack is full");
            top--;
        }
    }
    void pop()
    {
        try
        {
            int x=arr[top];
            top--;
            System.out.println("popped"+x);
        }
        catch(ArrayIndexOutOfBoundsException exp)
        {
            System.out.println("stack is empty");
            top++;
        }
    }
}
class q1
{
    public static void main(String args[])
    {
        Stack st = new Stack();
        int ch=0;
        while(ch!=3)
        {
            Scanner sc=new Scanner(System.in);
            System.out.println("enter choice\n1 for push\n2 for pop\n3 for exit");
            ch=sc.nextInt();
            if(ch==1)
            {
                System.out.println("enter the elements to be pushed");
                int x=sc.nextInt();
                st.push(x);
            }
            else if(ch==2)
            {
                st.pop();
            }
            else if(ch==3)
            {
                System.out.println("bye bye");
            }
        }
    }
}