#include<stdio.h>
#include<mpi.h>
int calc(int arr[],int x)
{
    int a=0;
    for(int i=0;i<3;i++)
    {
        if(arr[i]==x)
        {
            a++;
        }
    }
    return a;
}
int main(int argc, char ** argv)
{
    int ar[3],res,r,s,x;
    int arr[3][3] = {
        {1, 2, 3},
        {4, 3, 6},
        {7, 8, 9}
    };
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&r);
    MPI_Comm_size(MPI_COMM_WORLD,&s);
    if (r==0)
    {
        printf("enter the number to be searched\n");
        scanf("%d",&x);
    }
    MPI_Bcast(&x,1,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Scatter(arr,3,MPI_INT,ar,3,MPI_INT,0,MPI_COMM_WORLD);
    int op=calc(ar,x);
    printf("no of hit for %d in process %d is %d\n",x,r,op);
    MPI_Reduce(&op,&res,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
    if(r==0)
    {
        printf("total no of occurances is %d\n",res);
    }
    MPI_Finalize();
    return 0;
}