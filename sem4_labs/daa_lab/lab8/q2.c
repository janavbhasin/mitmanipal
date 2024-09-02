#include"heap.h"
int main()
{
    int n;
    printf("enter the size of the array \n");
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    heapify_sort(arr,n);
    printf("sorted array\n");
    print_array(arr,n);
    printf("\nopcount is:%d",op_counter);
}