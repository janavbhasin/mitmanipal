#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[])
{
    int r, s, length, n = 3;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    char A[s * n], B[s * n], *strA, *strB, result[2 * n * s+1]; 
    if (r == 0)
    {
        printf("Enter string of length %d : ", s * n);
        scanf("%s", A);
        printf("Enter string of length %d : ", s * n);
        scanf("%s", B);
        length = strlen(A);
        length /= s;
    }
    MPI_Bcast(&length, 1, MPI_INT, 0, MPI_COMM_WORLD);
    strA = (char *)calloc(length, sizeof(char));
    strB = (char *)calloc(length, sizeof(char));
    MPI_Scatter(A, length, MPI_CHAR, strA, length, MPI_CHAR, 0, MPI_COMM_WORLD);
    MPI_Scatter(B, length, MPI_CHAR, strB, length, MPI_CHAR, 0, MPI_COMM_WORLD);
    char sendStr[2 * length + 1];
    sendStr[0] = '\0';
    int i = 0, j = 0, k = 0;
    while (i < length || j < length)
    {
        if (k % 2 == 0)
        {
            sendStr[k++] = strA[i++];
        }
        else
        {
            sendStr[k++] = strB[j++];
        }
    }
    sendStr[k] = '\0';
    MPI_Gather(sendStr, 2 * length, MPI_CHAR, result, 2 * length, MPI_CHAR, 0, MPI_COMM_WORLD);
    if (r == 0)
    {
        result[2 * n * s] = '\0';
        printf("The result is : ");
        for(int i = 0; i<2*n*s; i++)
        {
            printf("%c", result[i]);
        }
        printf("\n");
    }
    free(strA);
    free(strB);
    MPI_Finalize();
    return 0;
}