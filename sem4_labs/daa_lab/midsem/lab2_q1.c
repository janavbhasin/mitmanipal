#include<stdio.h>
int min(int m,int n)
{
    if(m>n)
    {
        return n;
    }
    return m;
}
int gcd(int m,int n)
{
    int t=min(m,n);
    while(t!=0)
    {
        if(m%t==0)
        {
            if(n%t==0)
            {
                return t;
            }
        }
        t=t-1;
    }
    return 1;
}
int main()
{
    printf("enter 2 numbers\n");
    int a,b;
    scanf("%d%d",&a,&b);
    printf("gcd is %d\n",gcd(a,b));
}