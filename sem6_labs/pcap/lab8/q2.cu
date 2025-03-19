#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
__global__ void row (int* A, int* B, int* C, int wa, int wb) 
{
    int ro = threadIdx.x, val;
    for (int co = 0; co < wb; co++) 
    {
        val = 0;
        for (int k = 0; k < wa; k++) 
        {
            val += A[ro * wa + k] * B[k * wb + co];
        }
        C[ro * wb + co] = val;
    }
}
__global__ void col (int* A, int* B, int* C, int ha, int wa) 
{
    int co = threadIdx.x, val;
    int wb = blockDim.x;
    for (int ro = 0; ro < ha; ro++) 
    {
        val = 0;
        for (int k = 0; k < wa; k++) 
        {
            val += A[ro * wa + k] * B[k * wb + co];
        }
        C[ro * wb + co] = val;
    }
}
__global__ void ele (int* A, int* B, int* C, int wa) 
{
    int ro = threadIdx.x, co = threadIdx.y;
    int wb = blockDim.y;
    int val = 0;
    for (int k = 0; k < wa; k++) 
    {
        val += A[ro * wa + k] * B[k * wb + co];
    }
    C[ro * wb + co] = val;
}
__host__ void disp (int *mat, int h, int w) 
{
    for (int i = 0; i < h; i++) 
    {
        for (int j = 0; j < w; j++)
        {
            printf("%d ", mat[i * w + j]);
        }
        printf("\n");
    }
}
int main () 
{
    int ha, wa, hb, wb;
    printf("Enter number of rows of matrix A: ");
    scanf(" %d", &ha);
    printf("Enter number of columns of matrix A: ");
    scanf(" %d", &wa);
    printf("Enter number of rows of matrix B: ");
    scanf(" %d", &hb);
    printf("Enter number of columns of matrix B: ");
    scanf(" %d", &wb);
    int *A, *B, *C;
    cudaMallocManaged(&A, ha * wa * sizeof(int));
    cudaMallocManaged(&B, hb * wb * sizeof(int));
    cudaMallocManaged(&C, ha * wb * sizeof(int));
    printf("Enter %d elements of matrix A:\n", ha * wa);
    for (int i = 0; i < ha * wa; i++)
    {
        scanf(" %d", &A[i]);
    }
    printf("Enter %d elements of matrix B:\n", hb * wb);
    for (int i = 0; i < hb * wb; i++) 
    {
        scanf(" %d", &B[i]);
    }
    int x = -1;
    while (1) 
    {
        printf("\n1: Row-wise \n2: Column-wise \n3: Element-wise \n0: Exit \nEnter method to use for multiplication: ");
        scanf(" %d", &x);
        if (x == 0) 
        {
            printf("Exiting...\n");
            break;
        }
        if (x == 1)
        {
            row <<< 1, ha >>> (A, B, C, wa, wb);
        }
        else if (x == 2)
        {
            col <<< 1, wb >>> (A, B, C, ha, wa);
        }
        else 
        {
            dim3 blockDim(ha, wb);
            ele <<< 1, blockDim >>> (A, B, C, wa);
        }
        cudaDeviceSynchronize();
        printf("\nResultant matrix C:\n");
        disp(C, ha, wb);
    }
}