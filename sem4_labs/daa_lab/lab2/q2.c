#include <stdio.h>
int opcount=0;
int prime(int n) 
{
    if (n == 2) 
    {
        opcount++;
        return 0;
    }
    for (int i = 2; i * i <= n; i++) 
    {
        opcount++;
        if (n % i == 0) 
        {
            return 1;
        }   
    }
    return 0;
}
int gcd(int x, int y) 
{
    int arr1[x], arr2[y], i, j = 0, copy1 = x, copy2 = y;
    for (i = 2; i <= x; i++) 
    {
        if (prime(i) == 0) 
        {
            while (copy1 % i == 0) 
            {
                arr1[j] = i;
                copy1 = copy1 / i;
                j++;
                opcount++;
            }
        }
    }
    arr1[j] = -1;
    j = 0;
    for (i = 2; i <= y; i++) 
    {
        if (prime(i) == 0) 
        {
            while (copy2 % i == 0) 
            {
                arr2[j] = i;
                copy2 = copy2 / i;
                j++;
                opcount++;
            }
        }
    }
    arr2[j] = -1;
    int size1 = 0;
    while (arr1[size1] != -1) 
    {
        size1++;
    }
    int size2 = 0;
    while (arr2[size2] != -1) 
    {
        size2++;
    }
    int commonArray[size1 + size2+1];
    int commonSize = 0,k=0;
    i = 0;
    j = 0;
    while (i < size1 && j < size2) 
    {
        opcount++;
        if (arr1[i] == arr2[j]) 
        {
            commonArray[k++] = arr1[i];
            i++;
            j++;
        } 
        else if (arr1[i] < arr2[j]) 
        {
            i++;
        } 
        else 
        {
            j++;
        }
    }
    commonArray[k] = -1;
    int gccd=1;
    for (i = 0; commonArray[i]!=-1; i++) 
    {
        gccd=commonArray[i]*gccd;
    }
    printf("\nopcount is %d\n",opcount);
    return gccd;
}
int main() 
{
    int m, n;
    printf("Enter two numbers: ");
    scanf("%d %d", &m, &n);
    printf("m+n:%d\n",m+n);
    printf("gcd is %d",gcd(m, n));
}