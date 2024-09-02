#include<stdio.h>
#include<stdlib.h>
void floyd(int**arr,int n)
{
    int i,j,k,flag;
    for(k=0;k<n;k++)
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                arr[i][j]=(arr[i][j]<(arr[i][k]+arr[k][j]))?arr[i][j]:(arr[i][k]+arr[k][j]);
            }
        }
    }
}
int main()
{
    int i,j,n;
    printf("enter no of vertices: ");
    scanf("%d",&n);
    int**arr=(int**)malloc(n*sizeof(int*));
    for(i=0;i<n;i++)
    {
        arr[i]=(int*)malloc(n*sizeof(int));
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    floyd(arr,n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d  ",arr[i][j]);
        }
        printf("\n");
    }
}