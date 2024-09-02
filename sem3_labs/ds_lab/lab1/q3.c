#include<stdio.h>
int l_search(int arr[],int num,int search)
{
    for (int i=0;i<num;i++)
    {
        if(arr[i]==search)
        {
            return i;
        }
    }
    return 999;
}
int main()
{
    int num,arr[10],search;
    printf("enter the number of elements");
    scanf("%d",&num);
    printf("enter the array in ascending order");
    for(int i=0;i<num;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter the number to be searched");
    scanf("%d",&search);
    int a=l_search(arr,num,search);
    if(a==999)
    {
        printf("element not found");
    }
    else
    {
        printf("the element is at %d place",a+1);
    }
}