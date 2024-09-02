#include <stdio.h>
#include <stdlib.h> 
void merge(int arr[],int l,int m,int r)
{
    int n1=m-l+1;
    int n2=r-m;
    int L[n1],R[n2];
    for(int i=0;i<n1;i++)
    {
        L[i]=arr[l+i];
    }
    for (int i = 0; i < n2; i++) 
    {
        R[i] = arr[m + 1 + i];
    }
    int i=0,j=0,k=l;
    while(i<n1 && j<n2)
    {
        if(L[i]<=R[j])
        {
            arr[k]=L[i];
            i++;
        }
        else
        {
            arr[k]=R[j];
            j++;
        }
        k++;
    }
    while(i<n1)
    {
        arr[k]=L[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        arr[k]=R[j];
        j++;
        k++;
    }
}
void Mergesort(int arr[],int l,int r)
{
    if(l<r)
    {
        int m=l+(r-l)/2;
        Mergesort(arr,l,m);
        Mergesort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}
void printArray(int arr[], int size) 
{
    int i;
    for (i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main() 
{
    int arr_size;
    printf("Enter size of array: ");
    scanf("%d", &arr_size);
    int arr[arr_size];
    printf("Enter elements of the array: ");
    for (int i = 0; i < arr_size; i++) 
    {
        scanf("%d", &arr[i]); 
    }
    printf("Given array is \n");
    printArray(arr, arr_size);
    Mergesort(arr, 0, arr_size - 1);
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
