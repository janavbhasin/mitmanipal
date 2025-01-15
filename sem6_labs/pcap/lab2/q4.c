#include <mpi.h>
#include <stdio.h>
int main(int argc,char**argv)
{
    int r, s;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &r);
	MPI_Comm_size(MPI_COMM_WORLD, &s);
    int n;
    if(r==0)
    {
        printf("enter number: ");
        scanf("%d",&n);
        printf("P%d: Sending %d to P%d\n", r, n, r + 1);
        MPI_Send(&n,1,MPI_INT,r+1,r+1,MPI_COMM_WORLD);
        MPI_Recv(&n,1,MPI_INT,s-1,r,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        printf("P%d: Received %d from P%d\n", r, n, s - 1);
    }
    else
    {
        MPI_Recv(&n,1,MPI_INT,r-1,r,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        printf("P%d: Received %d from P%d\n", r, n, r - 1);
        n++;
        printf("P%d: Sending %d to P%d\n", r, n, (r + 1) % s);
        MPI_Send(&n,1,MPI_INT,(r+1)%s,(r+1)%s,MPI_COMM_WORLD);
    }
    MPI_Finalize();
    return 0;
}