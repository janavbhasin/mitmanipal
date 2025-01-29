#include<stdio.h>
#include<mpi.h>
void error(int err)
{
    if(err!=MPI_SUCCESS)
    {
        char er[BUFSIZ];
        int len,cl;
        MPI_Error_class(err,&cl);
        MPI_Error_string(err,er,&len);
        printf("ERROR: %d %s\n",cl,er);
    }
}
int main(int argc,char **argv)
{
    int e,r,s,fact=1,sum;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&r);
    MPI_Comm_size(MPI_COMM_WORLD,&s);
    MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
    //e=MPI_Comm_size(MPI_COMM_NULL,&s);
    e=MPI_Comm_size(MPI_COMM_WORLD,&s);
    if(r==0)
    {
        sum=0;
        error(e);
    }
    int se=r+1;
    e=MPI_Scan(&se,&fact,1,MPI_INT,MPI_PROD,MPI_COMM_WORLD);
    if(r==0)
    {
        error(e);
    }
    e=MPI_Scan(&fact,&sum,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
    if(r==0)
    {
        error(e);
    }
    if(r==s-1)
    {
        printf("factorial sum till %d is %d\n",r+1,sum);
    }
    MPI_Finalize();
    return 0;
}