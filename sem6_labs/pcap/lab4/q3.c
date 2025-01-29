#include <stdio.h>
#include <mpi.h>
#define N 4
int main(int argc, char **argv) 
{
    int r, s;
    int fmat[N][N],mat[N][N] = {
        {1, 2, 3, 4},
        {1, 2, 3, 1},
        {1, 1, 1, 1},
        {2, 1, 2, 1}
    };
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    int nmat[N],xmat[N];
    MPI_Scatter(mat,4,MPI_INT,nmat,4,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Scan(nmat,xmat,4,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
    MPI_Gather(xmat,4,MPI_INT,fmat,4,MPI_INT,0,MPI_COMM_WORLD);
    if (r==0)
    {
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                printf("%d\t",fmat[i][j]);
            }
            printf("\n");
        }
    }
    MPI_Finalize();
    return 0;
}