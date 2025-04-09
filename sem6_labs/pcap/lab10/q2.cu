#include <stdio.h>
#include <cuda_runtime.h>
#define N 10
#define K 5
#define BLOCK_SIZE 256
__constant__ int d_kernel[K];
__global__ void conv1D(int *d_input, int *d_output, int n, int k)
{
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    int radius = k / 2;

    int sum = 0;
    if (tid < n)
    {
        for (int j = -radius; j <= radius; ++j)
        {
            int idx = tid + j;
            if (idx >= 0 && idx < n)
            {
                sum += d_input[idx] * d_kernel[j + radius];
            }
        }
        d_output[tid] = sum;
    }
}
void initializeData(int *input, int *kernel, int n, int k)
{
    for (int i = 0; i < n; ++i)
    {
        input[i] = rand() % 10;
    }
    for (int i = 0; i < k; ++i)
    {
        kernel[i] = 1;
    }
}
void printArray(int *arr, int n)
{
    for (int i = 0; i < n; ++i)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main()
{
    int *h_input, *h_kernel, *h_output;
    int size_input = N * sizeof(int);
    int size_output = N * sizeof(int);
    cudaMallocManaged(&h_input, size_input);
    cudaMallocManaged(&h_kernel, K * sizeof(int));
    cudaMallocManaged(&h_output, size_output);
    initializeData(h_input, h_kernel, N, K);
    cudaMemcpyToSymbol(d_kernel, h_kernel, K * sizeof(int));
    int gridSize = (N + BLOCK_SIZE - 1) / BLOCK_SIZE;
    dim3 blockDim(BLOCK_SIZE);
    dim3 gridDim(gridSize);
    conv1D<<<gridDim, blockDim>>>(h_input, h_output, N, K);
    cudaDeviceSynchronize();
    printf("Input Array:\n");
    printArray(h_input, N);
    printf("\nKernel Array:\n");
    printArray(h_kernel, K);
    printf("\nResult of 1D Convolution:\n");
    printArray(h_output, N);
}