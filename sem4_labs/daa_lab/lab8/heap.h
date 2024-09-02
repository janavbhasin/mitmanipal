#include<stdio.h>
int op_counter = 0;
void heapify(int arr[],int i)
{
    int parent=(i-1)/2;
    if(arr[parent] < arr[i] && parent >= 0)
    {
        op_counter++;
        int temp=arr[parent];
        arr[parent]=arr[i];
        arr[i]=temp;
        heapify(arr,parent);
    }
    op_counter++;
}
void create_heap(int arr [],int n)
{
    for (int i=0;i<n;i++)
    {
        heapify(arr,i);
    }
}
void print_array(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }
}
void heapify_sort(int arr[],int n)
{
    create_heap(arr,n);
    for(int i=n-1;i>0;i--)
    {
        op_counter++;                                                                                                  
        int temp=arr[0];
        arr[0]=arr[i];
        arr[i]=temp;
        create_heap(arr,i);
    }
}