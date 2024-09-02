#include<stdio.h>
int max(int a,int b)
{
    if(a>b)
    {
        return a;
    }
    return b;
}
int main()
{
    int a[10][10]={0};
    int w[]={0,2,1,3,2};   
    int val[]={0,12,10,20,15}; 
    int kn[10];
    int i,j,k,n=4,W=5;
    for(i=1;i<n+1;i++)
    {
        for(j=1;j<W+1;j++)
        {
            if(j<w[i])
            {
                a[i][j]=a[i-1][j];
            }
            else
            {
                a[i][j]=max(a[i-1][j],val[i]+a[i-1][j-w[i]]);
            }
        }
    }
    for(i=0;i<n+1;i++)
    {
        for(j=0;j<W+1;j++)
        {
            printf("%d  ",a[i][j]);
        }
        printf("\n");
    }
}