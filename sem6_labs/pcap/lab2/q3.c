#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv)
{
    int r, s;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    if(r==0)
    {
        int arr[s-1];
        printf("enter %d elements: ",s-1);
        for(int i=0;i<s-1;i++)
        {
            scanf("%d",&arr[i]);
        }
        int buff=MPI_BSEND_OVERHEAD +sizeof(int)*s-1;
        char*buffer=(char*)malloc(buff);
        MPI_Buffer_attach(buffer,buff);
        for(int i=0;i<s-1;i++)
        {
            MPI_Bsend(&arr[i],1,MPI_INT,i+1,i+1,MPI_COMM_WORLD);
            printf("sending %d in P%d\n",arr[i],r);
        }
        MPI_Buffer_detach(&buffer,&buff);
    }
    else
    {
        int n;
        MPI_Recv(&n,1,MPI_INT,0,r,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        if(r%2==0)
        {
            printf("P%d sq %d\n",r,n*n);
        }
        else
        {
            printf("P%d cube %d\n",r,n*n*n);
        }
    }
    MPI_Finalize();
    return 0;
}