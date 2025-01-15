#include<mpi.h>
#include<stdio.h>
int main(int argc, char**argv)
{
	int r,s,x;
	int n1=5;
	int n2=4;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&r);
	MPI_Comm_size(MPI_COMM_WORLD,&s);
	if (r==0)
	{
		x=n1+n2;
	}
	else if (r==1)
	{
		x=n1-n2;
	}
	else if (r==2)
	{
		x=n1*n2;
	}	
	else if (r==3)
	{
		x=n1/n2;
	}
	printf("rank=%d  %d\n",r,x);
	MPI_Finalize();
	return 0;
}
//rank=2 20
//rank=3 1
//rank=0 9
//rank=1 1