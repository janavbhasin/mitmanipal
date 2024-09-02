#include <stdio.h>
#include <stdlib.h>
void reverse(int *arr,int length)
{
    for(int i=0;i<length/2;i++)
    {
        int temp=arr[length-i-1];
        arr[length-i-1]=arr[i];
        arr[i]=temp;
    }
}
int main()
{
    int *arr=NULL,length;
    printf("enter the number of elements in the array:length");
    scanf("%d",&length);
    arr=(int *)malloc(length*sizeof(int));
    printf("enter the elements:length");
    for(int i=0;i<length;i++)
    {
        scanf("%d",&arr[i]);
    }
    reverse(arr,length);
    printf("the reversed elements are:length");
    for(int i=0;i<length;i++)
    {
        printf("%dlength",arr[i]);
    }
    free(arr);
}