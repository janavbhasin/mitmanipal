#include<stdio.h>
#include<stdlib.h>
void heapify(int arr[],int n)
{
    int parent=(n-1)/2;
    if(parent >=0 && arr[parent] < arr[n])
    {
        int t=arr[n];
        arr[n]=arr[parent];
        arr[parent]=t;
        heapify(arr,parent);
    } 
}
void create_heap(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        heapify(arr,i);
    }
}
void print_arr(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }
}
void heap_sort(int arr[],int n)
{
    create_heap(arr,n);
    for(int i=n-1;i>0;i--)
    {
        int temp=arr[0];
        arr[0]=arr[i];
        arr[i]=temp ;
        create_heap(arr,i);
    }
}