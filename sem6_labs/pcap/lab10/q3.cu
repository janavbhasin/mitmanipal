#include <stdio.h>
#include <cuda_runtime.h>
#define N 10
#define BLOCK_SIZE 256
__global__ void inclusiveScan(int *d_in, int *d_out, int n)
{
    __shared__ int temp[BLOCK_SIZE];
    int tid = threadIdx.x;
    int global_tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (global_tid < n)
    {
        temp[tid] = d_in[global_tid];
    }
    else
    {
        temp[tid] = 0;
    }
    __syncthreads();
    for (int offset = 1; offset < blockDim.x; offset *= 2)
    {
        int val = 0;
        if (tid >= offset)
        {
            val = temp[tid - offset];
        }
        __syncthreads();
        temp[tid] += val;
        __syncthreads();
    }
    if (global_tid < n)
    {
        d_out[global_tid] = temp[tid];
    }
}
void initializeArray(int *arr, int n)
{
    for (int i = 0; i < n; ++i)
    {
        arr[i] = 1;
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
    int h_in[N], h_out[N];
    int *d_in, *d_out;
    int size = N * sizeof(int);
    initializeArray(h_in, N);
    cudaMalloc((void **)&d_in, size);
    cudaMalloc((void **)&d_out, size);
    cudaMemcpy(d_in, h_in, size, cudaMemcpyHostToDevice);
    dim3 blockDim(BLOCK_SIZE);
    dim3 gridDim((N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    inclusiveScan<<<gridDim, blockDim>>>(d_in, d_out, N);
    cudaMemcpy(h_out, d_out, size, cudaMemcpyDeviceToHost);
    printf("Input Array:\n");
    printArray(h_in, N);
    printf("\nInclusive Scan Result:\n");
    printArray(h_out, N);
}