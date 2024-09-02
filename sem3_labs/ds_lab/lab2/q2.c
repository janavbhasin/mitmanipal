#include <stdio.h>
#include <stdlib.h>
int smallest(int *arr,int length)
{
    int smallest=arr[0];
    for(int i=0;i<length;i++)
    {
        if (smallest>=arr[i])
        {
            smallest=arr[i];
        }
    }
    return smallest;
}
int main()
{
    int *arr=NULL, length;
    printf("enter the size of the array:\n");
    scanf("%d",&length);
    arr=(int*)malloc(length*sizeof(int));
    printf("enter the elements:\n");
    for(int i=0;i<length;i++)
    {
        scanf("%d",&arr[i]);
    }
    int smallest_no=smallest(arr,length);
    printf("the smallest no is : %d",smallest_no);
}