#include <mpi.h>
#include <stdio.h>
int main(int argc, char**argv)
{
	int r, s, n;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &r);
	MPI_Comm_size(MPI_COMM_WORLD, &s);
	if(r == 0)
    {
		for(int i = 1; i<s; i++)
        {
			MPI_Send(&i, 1, MPI_INT, i, i, MPI_COMM_WORLD);
            printf("send %d in p%d\n", i, r);
        }
	}
	else
    {
		MPI_Recv(&n, 1, MPI_INT, 0, r, MPI_COMM_WORLD, MPI_STATUS_IGNORE );
		printf("received %d in p%d\n", n, r);
	}
	MPI_Finalize();
	return 0;
}