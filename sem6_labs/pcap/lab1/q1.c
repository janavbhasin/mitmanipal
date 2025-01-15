#include <mpi.h>
#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
    int r, s;
    double x = 2.0;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    double re = pow(x, r);
    printf("Process %d of %d: pow(%.2f, %d) = %.2f\n", r, s, x, r, re);
    MPI_Finalize();
    return 0;
}
// Process 0 of 4: pow(2.00, 0) = 1.00
//Process 2 of 4: pow(2.00, 2) = 4.00
//Process 1 of 4: pow(2.00, 1) = 2.00
//Process 3 of 4: pow(2.00, 3) = 8.00