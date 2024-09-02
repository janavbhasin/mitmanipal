#include <stdio.h>
#include <stdbool.h>
bool partition(int arr[],int n)
{
    int i,sum=0,j;
    for(i=0;i<n;i++)
    {
        sum+=arr[i];
    }
    if(sum%2==1)
    {
        return false;
    }
    else
    {
        int half=sum/2;
        for(int i=0;i<(1<<n);i++)
        {
            int currentsum=0;
            for(j=0;j<n;j++)
            {
                
                if(i&(1<<j))
                {
                    currentsum+=arr[j];
                }
            }
            if(half==currentsum)
            {
                return true;
            }
        }
    }
    return false;
}
int main()
{
    int arr[1000],n;
    printf("enter the no of elements in the array\n");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    if(partition(arr,n)==true)
    {
        printf("possible\n");
    }
    else
    {
        printf("not possible\n");
    }
}