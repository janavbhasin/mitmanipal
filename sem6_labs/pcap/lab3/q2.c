#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>
int main(int argc,char**argv) 
{
    int r,s,*n,*arr,res,m;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&r);
    MPI_Comm_size(MPI_COMM_WORLD,&s);
    if (r==0)
    {
        printf("enter m: ");
        scanf("%d",&m);
        n=(int*)calloc(s*m,sizeof(int));
        printf("enter %d numbers: ",s*m);
        for(int i=0;i<s*m;i++)
        {
            scanf("%d",&n[i]);
        }
    }
    MPI_Bcast(&m,1,MPI_INT,0,MPI_COMM_WORLD);
    arr=(int*)calloc(m,sizeof(int));
    MPI_Scatter(n,m,MPI_INT,arr,m,MPI_INT,0,MPI_COMM_WORLD);
    int S=0;
    for(int i=0;i<m;i++)
    {
        S+=arr[i];  
    }
    float local_avg = (float)S / m;
    printf("Process %d, Local average: %.2f\n", r, local_avg);
    int *partial_sums = NULL;
    if (r == 0) 
    {
        partial_sums = (int*)calloc(s, sizeof(int));
    }
    MPI_Gather(&S, 1, MPI_INT, partial_sums, 1, MPI_INT, 0, MPI_COMM_WORLD);
    if (r == 0) 
    {
        int total_sum = 0;
        for (int i = 0; i < s; i++) 
        {
            total_sum += partial_sums[i];
        }
        int overall_avg = total_sum / (s * m);  
        printf("Overall average: %d\n", overall_avg);
        free(partial_sums);
        free(n);
    }
    free(arr);
    MPI_Finalize();
    return 0;
}