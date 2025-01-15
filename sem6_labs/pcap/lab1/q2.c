#include<mpi.h>
#include<stdio.h>
int main(int argc, char** argv)
{
	int r,s;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    if(r%2==0)
    {
    	printf("rank=%d hello\n",r);
    }
    else
    {
    	printf("rank=%d world\n",r);
    }
    MPI_Finalize();
    return 0;
}
//rank=0 hello
//rank=1 world
//rank=2 hello
//rank=3 world