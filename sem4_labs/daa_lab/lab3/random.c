#include <stdio.h>
#include <stdbool.h>
int arraySum(int arr[], int n) 
{
    int sum = 0;
    for (int i = 0; i < n; i++) 
	{
        sum += arr[i];
    }
    return sum;
}
bool isPartitionPossible(int arr[], int n, int subsetSum, int index, int subset1Sum) 
{
    if (index == n) 
	{
        return subset1Sum == subsetSum;
    }
    if (isPartitionPossible(arr, n, subsetSum, index + 1, subset1Sum + arr[index])) 
	{
        return true;
    }
    return isPartitionPossible(arr, n, subsetSum, index + 1, subset1Sum);
}
bool canPartition(int arr[], int n) 
{
	
    int totalSum = arraySum(arr, n);
    if (totalSum % 2 != 0) 
	{
        return false;
    }
    return isPartitionPossible(arr, n, totalSum / 2, 0, 0);
}
int main() {
    int arr[] = {3, 1, 1, 9, 12};
    int n = sizeof(arr) / sizeof(arr[0]);
    if (canPartition(arr, n)) 
	{
        printf("Partition is possible\n");
    } 
	else 
	{
        printf("Partition is not possible\n");
    }
}