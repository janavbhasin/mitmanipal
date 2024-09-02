#include<stdio.h>
int summed(int arr[],int n)
{
    int sum=0;
    for(int i=0;i<n;i++)
    {
        sum=sum+arr[i];
    }
    return sum;
}
int partitionpossible(int arr[],int n,int index,int sum,int subset)
{
    if(index==n)
    {
        if(sum==subset)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if(partitionpossible(arr,n,index+1,sum,subset+arr[index])==1)
    {
        return 1;
    }
    if(partitionpossible(arr,n,index+1,sum,subset)==1)
    {
        return 1;
    }
    return 0;
}
int partition(int arr[],int n)
{
    int sum=summed(arr,n);
    if(sum%2==1)
    {
        return 0;
    }
    else
    {
        return partitionpossible(arr,n,0,sum/2,0);
    }
}
int main() {
    int arr[] = {3, 1, 1, 9, 12};
    int n = sizeof(arr) / sizeof(arr[0]);
    if (partition(arr, n)==1) 
	{
        printf("Partition is possible\n");
    } 
	else 
	{
        printf("Partition is not possible\n");
    }
}