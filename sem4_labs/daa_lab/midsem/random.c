#include<stdio.h>
int op=0;
int max=-1e9;
int min=1e9;
void swap(int arr[],int a,int b)
{
	int temp=arr[a];
	arr[a]=arr[b];
	arr[b]=temp;
}
void quicksort(int arr[],int start ,int end)
{
	if(end-start<=1)
	{
		return;
	}
	int pivot=arr[start];
    if(max<pivot)    
    {
        max=pivot;
    }
    if(min>pivot)
    {
        min=pivot;
    }
	int i=start+1,j=end-1;
	while(i<=j)
	{
		while(i<=j && arr[j]>=pivot)
		{
			j--;
			op++;
		}
		while(i<=j && arr[i]<=pivot)
		{
			i++;
			op++;
		}
		if(i>=j)
		{
			continue;
		}
		swap(arr,i,j);
	}
	swap(arr,start,j);
	quicksort(arr,start,j);
	quicksort(arr,j+1,end);
}
void printArray(int arr[], int size) 
{
    for (int i = 0; i < size; i++)
	{
        printf("%d ", arr[i]);
	}
    printf("\n");
}
int main() 
{
    int n;
    printf("enter the number of elements in the array\n");
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements\n");
    for(int i=0;i<n;i++)
    {
    	scanf("%d",&arr[i]);
    }
    printf("Unsorted array: \n");
    printArray(arr, n);
    quicksort(arr, 0, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    printf("\nopcount is %d",op);
    printf("max is %d\n",max);
    printf("min is %d\n",min);
}