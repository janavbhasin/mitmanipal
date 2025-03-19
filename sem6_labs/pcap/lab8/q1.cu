#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
__global__ void mataddrow(int*a,int*b,int*c,int wa)
{
    int ro=threadIdx.x;
    for(int co=0;co<wa;co++)
    {
        c[ro*wa+co]=a[ro*wa+co]+b[ro*wa+co];
    }
}
__global__ void mataddcolumn(int*a,int*b,int*c,int ha)
{
    int co=threadIdx.x,wa=blockDim.x;
    for(int ro=0;ro<ha;ro++)
    {
        c[ro*wa+co]=a[ro*wa+co]+b[ro*wa+co];
    }
}
__global__ void mataddelement(int*a,int*b,int*c)
{
    int ro=threadIdx.x,co=threadIdx.y,wa=blockDim.y;
    c[ro*wa+co]=a[ro*wa+co]+b[ro*wa+co];
}
__host__ void displayMatrix (int *mat, int h, int w) 
{
    for (int i=0; i<h; i++) 
    {
        for (int j=0; j<w; j++) 
        {
            printf("%d ", mat[i * w + j]);
        }
        printf("\n");
    }
}
int main() 
{
    int ha, wa;
    printf("Enter number of rows and columns of matrix: ");
    scanf(" %d %d", &ha,&wa);
    int *A, *B, *C;
    cudaMallocManaged(&A, ha * wa * sizeof(int));
    cudaMallocManaged(&B, ha * wa * sizeof(int));
    cudaMallocManaged(&C, ha * wa * sizeof(int));
    printf("Enter %d elements of matrix A:\n", ha * wa);
    for (int i = 0; i < ha * wa; i++) 
    {
        scanf(" %d", &A[i]);
    }
    printf("Enter %d elements of matrix B:\n", ha * wa);
    for (int i = 0; i < ha * wa; i++)      
    {
        scanf(" %d", &B[i]);
    }
    int x = -1;
    while (1) 
    {
        printf("\n1: Row-wise \n2: Column-wise \n3: Element-wise \n0: Exit \nEnter method to use for addition: ");
        scanf(" %d", &x);
        if (x == 0)
        {
            printf("Exiting...\n");
            break;
        }
        if (x == 1)
        {
            mataddrow <<< 1, ha >>> (A, B, C, wa);
        }
        else if (x == 2)
        {
            mataddcolumn <<< 1, wa >>> (A, B, C, ha);
        }
        else 
        {
            dim3 blockDim(ha, wa);
            mataddelement <<< 1, blockDim >>> (A, B, C);
        }
        cudaDeviceSynchronize(); 
        printf("\nResultant matrix C:\n");
        displayMatrix(C, ha, wa);
    }
}