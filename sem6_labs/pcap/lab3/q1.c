#include<stdio.h>
#include<mpi.h>
int main(int argc,char**argv)
{
    int r,s,N,A[10],B[10],c,i,f;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&r);
    MPI_Comm_size(MPI_COMM_WORLD,&s);
    if (r==0)
    {
        N=s;
        fprintf(stdout,"Enter %d values: \n",N);
        fflush(stdout);
        for (i=0;i<N;i++)
        {
            scanf("%d",&A[i]);
        }
    }
    MPI_Scatter(A,1,MPI_INT,&c,1,MPI_INT,0,MPI_COMM_WORLD);
    fprintf(stdout, "Received %d in process %d\n", c, r);
	fflush(stdout);
    f=1;
    for(i=2;i<=c;i++)
    {
        f*=i;
    }
    MPI_Gather(&f,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD);
    if(r==0)
    {
        int S=0;
        for(i=0;i<=c;i++)
        {
            S+=B[i];
        }
        fprintf(stdout, "Sum of factorials is: %d\n", S);
		fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}