#include<mpi.h>
#include <stdio.h>
int fib(int n)
{
	if(n<=1)
	{
		return n;
	}
	int a=0,b=1,c;
	for (int i=2;i<=n;i++)
	{
		c=a+b;
		a=b;
		b=c;
	}
	return c;
}
int main(int argc, char **argv)
{
	int r,s,x=1;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&r);
	MPI_Comm_size(MPI_COMM_WORLD,&s);
	if (r%2==0)
	{
		for(int i=1;i<=r;i++)
		{
			x*=i;
		}
	}
	else
	{
		x=fib(r);
	}
	printf("rank=%d   %d\n",r,x);
	MPI_Finalize();
	return 0;
}