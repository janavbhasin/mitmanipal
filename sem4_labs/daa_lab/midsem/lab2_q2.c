#include<stdio.h>
int prime(int n)
{
    if(n==2)
    {
        return 0;
    }
    for(int i=2;(i*i)<=n;i++)
    {
        if(n%i==0)
        {
            return 1;
        }
    }
    return 0;
}
int gcd(int m,int n)
{
    int arr1[m],arr2[n],j=0,c1=m,c2=n;
    for(int i=2;i<=m;i++)
    {
        if(prime(i)==0)
        {
            while(c1%i==0)
            {
                arr1[j]=i;
                c1=c1/i;
                j++;
            }
        }
    }
    int size1=j;
    j=0;
    for(int i=2;i<=n;i++)
    {
        if(prime(i)==0)
        {
            while(c2%i==0)
            {
                arr2[j]=i;
                c2=c2/i;
                j++;
            }
        }
    }
    int size2=j;
    int gccd=1,i=0;
    j=0;
    while(i<size1&&j<size2)
    {
        if(arr1[i]==arr2[j])
        {
            gccd=gccd*arr1[i];
            i++;
            j++;
        }
        else if(arr1[i]<arr2[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }
    return gccd;
}
int main() 
{
    int m, n;
    printf("Enter two numbers: ");
    scanf("%d %d", &m, &n);
    printf("gcd is %d",gcd(m, n));
}