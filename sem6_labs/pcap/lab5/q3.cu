#include <stdio.h>
#include <math.h>
#include <cuda_runtime.h>
__global__ void calculateSine(float *a, float *sin, int n) 
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
    {
        sin[i] = sinf(a[i]);
    }
}
int main(void)
{
    int n;
    printf("Enter number of angles:\n");
    scanf("%d", &n);
    float*ha=(float*)malloc(sizeof(float)*n);
    float*hs=(float*)malloc(sizeof(float)*n);
    float *da,*ds;
    cudaMalloc((void**)&da,n*sizeof(float));
    cudaMalloc((void**)&ds,n*sizeof(float));
    printf("enter angles in radians:\n");
    for(int i=0;i<n;i++)
    {
        scanf("%f",&ha[i]);
    }
    cudaMemcpy(da,ha,n*sizeof(float),cudaMemcpyHostToDevice);
    int b = 256; 
    int nu =(n+b-1)/b;  
    calculateSine<<<nu,b>>>(da,ds,n);
    cudaMemcpy(hs,ds,n*sizeof(float),cudaMemcpyDeviceToHost);
    printf("Sine values are: \n");
    for (int i = 0; i < n; i++) 
    {
        printf("%f ", hs[i]);
    }
    printf("\n");
    free(ha);
    free(hs);
    cudaFree(da);
    cudaFree(ds);
    return 0;
}