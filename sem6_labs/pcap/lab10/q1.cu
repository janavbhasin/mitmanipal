#include <stdio.h>
#include <cuda_runtime.h>
#define N 4
__global__ void matrixMul(int *a, int *b, int *c, int n)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < n && col < n)
    {
        int sum = 0;
        for (int k = 0; k < n; ++k)
        {
            sum += a[row * n + k] * b[k * n + col];
        }
        c[row * n + col] = sum;
    }
}
void printMatrix(int *matrix, int n)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            printf("%d ", matrix[i * n + j]);
        }
        printf("\n");
    }
}
int main()
{
    int *a, *b, *c;
    int size = N * N * sizeof(int);
    cudaMallocManaged(&a, size);
    cudaMallocManaged(&b, size);
    cudaMallocManaged(&c, size);
    for (int i = 0; i < N * N; ++i)
    {
        a[i] = 1;
        b[i] = 2;
    }
    dim3 blockDim(2, 2);
    dim3 gridDim((N + blockDim.x - 1) / blockDim.x, (N + blockDim.y - 1) / blockDim.y);
    matrixMul<<<gridDim, blockDim>>>(a, b, c, N);
    cudaDeviceSynchronize();
    printf("Matrix A:\n");
    printMatrix(a, N);
    printf("\nMatrix B:\n");
    printMatrix(b, N);
    printf("\nResultant Matrix C (A x B):\n");
    printMatrix(c, N);
}