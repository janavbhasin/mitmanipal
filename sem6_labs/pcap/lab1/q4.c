#include <mpi.h>
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
char tog(char c)
{
	if(c>='A' && c<='Z')
	{
		return c+32;
	}
	return c-32;
}
int main(int argc,char *argv[])
{
	int r,s;
	char str[100];
	strcpy(str,argv[1]);
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&r);
	MPI_Comm_size(MPI_COMM_WORLD,&s);
	str[r]=tog(str[r]);
	printf("rank =%d , %c\n",r,str[r]);
	MPI_Finalize();
	return 0;
}
//rank =0 , H
//rank =1 , E
//rank =2 , L
//rank =3 , L