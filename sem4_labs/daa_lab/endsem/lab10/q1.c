#include<stdio.h>
#include<stdlib.h>
int warshall(int **arr,int n,int c)
{
    int flag;
    if(c==n)
    {
        for(int i=0;i<n;i++)
        {
            flag=1;
            for(int j=0;j<n;j++)
            {
                if(arr[i][j]==0)
                {
                    flag=0;
                }
            }
            if(flag==1)
            {
                return 1;
            }
        }
        return 0;
    }
    else
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(arr[i][j]==1||(arr[i][c]==1 && arr[c][j]==1))
                {
                    arr[i][j]=1;
                }
            }
        }
        return warshall(arr,n,c+1);
    }
}
int main()
{
    int i,j,n;
    printf("enter the no of vertices:");
    scanf("%d",&n);
    int ** arr=(int**)malloc(n*sizeof(int*));
    for(i=0;i<n;i++)
    {
        arr[i]=(int*)calloc(n,sizeof(int));
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    if(warshall(arr,n,0)==1)
    {
        printf("matrix exhibits transitivity\n");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%d  ",arr[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("matrix doesnt exhibit transitivity\n");
    }
}