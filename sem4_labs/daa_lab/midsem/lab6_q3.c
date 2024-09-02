#include<stdio.h>
void merge(int arr[],int m,int r,int l)
{
    int len1=m-l+1;
    int len2=r-m;
    int L[len1],R[len2];
    for(int i=0;i<len1;i++)
    {
        L[i]=arr[i+l];
    }
    for(int j = 0; j < len2; j++)
    {
        R[j] = arr[m + 1 + j];
    }
    int k=1,i=0,j=0;
    while(i<len1 &&j<len2)
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
    while(i<len1)
    {
        arr[k]=L[i];
        i++;
        k++;
    }
    while(j<len2)
    {
        arr[k]=R[j];
        j++;
        k++;
    }
}
void MergeSort(int arr[],int l,int r)
{
    int m;
    if(l<r)
    {
        m=l+(r-l)/2;
        MergeSort(arr,l,m);
        MergeSort(arr,m+1,r);
        merge(arr,m,r,l);
    }
}
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
 
int main()
{
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
 
    printf("Given array is \n");
    printArray(arr, arr_size);
 
    MergeSort(arr, 0, arr_size - 1);
 
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}