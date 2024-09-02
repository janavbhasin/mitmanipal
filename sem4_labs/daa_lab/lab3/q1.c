#include <stdio.h>
int main()
{
	int i,j,n,a[1000],t,op=0;
	printf("enter the no of elements\n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n-1;i++)
	{
		for (j=0;j<n-1-i;j++)
		{
			op++;
			if(a[j+1]<a[j])
			{
				t=a[j+1];
				a[j+1]=a[j];
				a[j]=t;
				op++;
			}
		}
	}
	printf("sorted array\n");
	for(i=0;i<n;i++)
	{
		printf("%d",a[i]);
	}
	printf("\nopcount is %d",op);
}