#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
__global__ void word_count(char *str, char *key, int *ind, int *res)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    int si = ind[idx], ei = ind[idx + 1], i = 0, i1 = 0, i2 = 0, is_eq = 1;
    char word[100];
    for (i = 0; i < (ei - si - 1); i++)
    {
        word[i] = str[si + 1 + i];
    }
    word[i] = '\0';
    while (word[i1] != '\0' && key[i2] != '\0')
    {
        if (word[i1] == key[i2])
        {
            i1++;
            i2++;
        }
        else
        {
            is_eq = 0;
            break;
        }
    }
    if (is_eq == 1 && key[i2] == '\0' && word[i1] == '\0')
    {
        atomicAdd(res, 1);
    }
}
int main()
{
    char str[100], key[20];
    printf("Enter the string: ");
    scanf(" %[^\n]s", str);
    printf("Enter key: ");
    scanf("%s", key);
    int i = 0, l1 = strlen(str), l2 = strlen(key), count = 1;
    for (i = 0; i < l1; i++)
    {
        if (str[i] == ' ')
        {
            count++;
        }
    }
    int res = 0, wi = 0, *ind = (int *)malloc((count + 1) * sizeof(int));
    ind[0] = -1;
    for (i = 0; i < l1; i++)
    {
        if (str[i] == ' ')
        {
            ind[++wi] = i;
        }
    }
    ind[++wi] = l1;
    char *d_str, *d_key;
    int *d_ind, *d_res;
    cudaMalloc((void **)&d_str, l1 * sizeof(char));
    cudaMalloc((void **)&d_key, l2 * sizeof(char));
    cudaMalloc((void **)&d_ind, (count + 1) * sizeof(int));
    cudaMalloc((void **)&d_res, sizeof(int));
    cudaMemcpy(d_str, str, l1 * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_key, key, l2 * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_ind, ind, (count + 1) * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_res, &res, sizeof(int), cudaMemcpyHostToDevice);
    word_count<<<1,count+1>>>(d_str, d_key, d_ind, d_res);
    cudaMemcpy(&res, d_res, sizeof(int), cudaMemcpyDeviceToHost);
    printf("Total occurrences of '%s' in '%s' is %d\n", key, str,res);
}                           