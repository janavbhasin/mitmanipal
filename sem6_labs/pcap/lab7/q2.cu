#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
__global__ void kernel(char* sin, int* sin_len, char* sout)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x,si=0;
    for (int i = 0; i < idx; i++)
    {
        si += (*sin_len)-i;
    }
    int total_chars = (*sin_len) - idx;
    for (int i = 0; i < total_chars; i++)
    {
        sout[si++] = sin[i];
    }
}    
int main()
{
    char sin[100], sout[100],* d_sin,* d_sout;
    printf("Enter s: ");
    scanf("%s", sin);
    int sin_len = strlen(sin),*d_sin_len,sout_len = 0;
    for (int i = 0; i < sin_len; i++)
    {
        sout_len += (i+1);
    }
    cudaMalloc((void**) &d_sin, sin_len * sizeof(char));
    cudaMalloc((void**) &d_sin_len, sizeof(int));
    cudaMalloc((void**) &d_sout, (sout_len + 1) * sizeof(char));
    cudaMemcpy(d_sin, sin, sin_len * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_sin_len, &sin_len, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_sout, sout, (sout_len + 1) * sizeof(char), cudaMemcpyHostToDevice);
    cudaEvent_t start, stop;
    float milliseconds = 0;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start);
    kernel <<<1, sin_len>>> (d_sin, d_sin_len, d_sout);
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&milliseconds, start, stop);
    cudaMemcpy(sout, d_sout, (sout_len + 1) * sizeof(char), cudaMemcpyDeviceToHost);
    sout[sout_len] = '\0';
    printf("rs: %s\n", sout);
    printf("Kernel execution time: %f ms\n", milliseconds);
}