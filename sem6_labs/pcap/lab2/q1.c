#include <string.h>
#include <mpi.h>
#include <stdio.h>
void toggle(int n,char*x)
{
    for (int i=0;i<n;i++)
    {
        if (x[i]>='a'&&x[i]<='z')
        {
            x[i]-=32;
        }
        else
        {
            x[i]+=32;
        }
    }
}
int main(int argc, char** argv)
{
    int r, s, l;
    char w[100];
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    MPI_Status status;
    if (r==0)
    {
        printf("Process %d: Enter the word: ", r);
        scanf("%s", w);
        l = strlen(w);
        MPI_Ssend(&l, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        MPI_Ssend(w, l, MPI_CHAR, 1, 1, MPI_COMM_WORLD);
        fprintf(stdout, "Process %d: Sending %s\n", r, w);
        MPI_Recv(w, l, MPI_CHAR, 1, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        fprintf(stdout, "Process %d: Received %s\n", r, w);
        fflush(stdout);
    }
    else
    {
        MPI_Recv(&l, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        MPI_Recv(w, l, MPI_CHAR, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        fprintf(stdout, "Process %d: Received %s\n", r, w);
        toggle(l, w);
        MPI_Ssend(w, l, MPI_CHAR, 0, 2, MPI_COMM_WORLD);
        fprintf(stdout, "Process %d: Sending toggled %s\n", r, w);
        fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}