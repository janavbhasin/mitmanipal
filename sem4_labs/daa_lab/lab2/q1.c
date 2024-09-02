#include<stdio.h>
int min(int a,int b)
{
	int min;
	if(a<b)
	{
		return a;
	}
	else
	{
		return b;
	}
}
int gcd(int m,int n)
{
	int t=min(m,n),opcount=0;
	while(t!=0)
	{
		opcount++;
		if(m%t==0)
		{
			if(n%t==0)
			{
				printf("opcount: %d\n",opcount);
				return t;
			}
			else
			{
				t=t-1;
			}
		}
		else
		{
			t=t-1;
		}
	}
}
int main()
{
	printf("enter the values of m and n\n");
	int m,n;
	scanf("%d",&m);
	scanf("%d",&n);
	printf("gcd is: %d",gcd(m,n));
}