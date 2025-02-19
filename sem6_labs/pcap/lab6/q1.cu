#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#define B 16
__global__ void conv(float *in, float *mask, float *out, int w, int mw) 
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    float sum = 0.0f;
    for (int j = 0; j < mw; j++) 
    {
        int idx = i + j - (mw - 1);
        if (idx >= 0 && idx < w) 
        {
            sum += in[idx] * mask[j];
        }
    }
    if (i < w) 
    { 
        out[i] = sum;
    }
}
void init(float *arr, int n, const char *msg) 
{
    printf("%s", msg);
    for (int i = 0; i < n; i++) 
    {
        scanf("%f", &arr[i]);
    }
}
int main() 
{
    int n, mw;
    printf("enter the size of array: ");
    scanf("%d", &n);
    printf("enter the size of mask: ");
    scanf("%d", &mw);
    float *N = (float *)malloc(n * sizeof(float));
    float *M = (float *)malloc(mw * sizeof(float));
    float *P = (float *)malloc(n * sizeof(float));
    float *d_in, *d_mask, *d_out;
    cudaMalloc(&d_in, n * sizeof(float));
    cudaMalloc(&d_mask, mw * sizeof(float));
    cudaMalloc(&d_out, n * sizeof(float));
    init(N, n, "enter array: ");
    init(M, mw, "enter mask: ");
    cudaMemcpy(d_in, N, n * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_mask, M, mw * sizeof(float), cudaMemcpyHostToDevice);
    dim3 a(n,1,1);
    dim3 b(1,1,1);
    conv<<<b, a>>>(d_in, d_mask, d_out, n, mw);
    cudaMemcpy(P, d_out, n * sizeof(float), cudaMemcpyDeviceToHost);
    for (int i = 0; i < n; i++) 
    {
        printf("%f\t", P[i]);
    }
    printf("\n");
}