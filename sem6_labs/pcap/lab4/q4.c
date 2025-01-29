#include <stdio.h>
#include <mpi.h>
int main(int argc, char **argv) 
{
    int r, s;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    char str[] = "PCAP"; 
    char rec; 
    char result[5];  
    MPI_Scatter(str, 1, MPI_CHAR, &rec, 1, MPI_CHAR, 0, MPI_COMM_WORLD);
    int repeat_count = r + 1; 
    for (int i = 0; i < repeat_count; i++) 
    {
        result[i] = rec;
    }
    result[repeat_count] = '\0'; 
    printf("process %d output is %s\n", r, result);
    char gathered[20] = {0};  
    if (r != 0) 
    {
        MPI_Send(result, repeat_count + 1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    } 
    else 
    {
        int offset = 0;  
        for (int i = 0; i < repeat_count; i++) 
        {
            gathered[offset++] = result[i];
        }
        for (int i = 1; i < s; i++) 
        {
            MPI_Recv(gathered + offset, i + 2, MPI_CHAR, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            offset += i + 1;  
        }
        printf("\nFinal gathered result: %s\n", gathered);
    }
    MPI_Finalize();
    return 0;
}
