#include<stdio.h>
#include <cuda_runtime.h>
#include <device_launch_parameters.h>
__global__ void vec_add(int*A,int*B,int*C,int n)
{
    int i=blockIdx.x*blockDim.x+threadIdx.x;
    if (i<n)
    {
        C[i]=A[i]+B[i];
    }
}
int main(void)
{
    int n;
    printf("enter no of elemnts:");
    scanf("%d",&n);
    int*a=(int*)malloc(n*sizeof(int));
    int*b=(int*)malloc(n*sizeof(int));
    int*c=(int*)malloc(n*sizeof(int));
    int *da,*db,*dc;
    cudaMalloc((void**)&da,n*sizeof(int));
    cudaMalloc((void**)&db,n*sizeof(int));
    cudaMalloc((void**)&dc,n*sizeof(int));
    printf("enter elements of vector 1:\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("enter elements of vector 2:\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&b[i]);
    }
    cudaMemcpy(da,a,n*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(db,b,n*sizeof(int),cudaMemcpyHostToDevice);
    int bl= 256;
    int num = (n + bl - 1) / bl;
    vec_add<<<num,bl>>>(da,db,dc,n);
    cudaMemcpy(c,dc,n*sizeof(int),cudaMemcpyDeviceToHost);
    printf("Result: \n");
    for (int i = 0; i < n; i++) 
    {
        printf("%d ", c[i]);
    }
    printf("\n");
    free(a);
    free(b);
    free(c);
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);
    return 0;
}