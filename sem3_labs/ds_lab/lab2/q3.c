#include<stdio.h>
#include<stdlib.h>
void multiplication(int**mrt1,int**mrt2,int**mrtf,int m,int n)
{
    for (int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            mrtf[i][j]=0;
            for(int k=0;k<n;k++)
            {
                mrtf[i][j]=mrtf[i][j]+(mrt1[i][k]*mrt2[k][j]);
            }
        }
    }
}
void inputmatrix(int **mtr,int m,int n)
{
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&mtr[i][j]);
        }
    }
}
int main()
{
    int **mtr1=NULL,**mtr2=NULL,**mtrf=NULL,m,n;
    printf("enter the order of the matrix:\n");
    scanf("%d%d",&m,&n);
    mtr1=(int**)calloc(m,sizeof(int*));
    mtr2=(int**)calloc(m,sizeof(int*));
    mtrf=(int**)calloc(m,sizeof(int*));
    for(int i=0;i<m;i++)
    {
        mtr1[i]=(int*)calloc(n,sizeof(int));
        mtr2[i]=(int*)calloc(n,sizeof(int));
        mtrf[i]=(int*)calloc(n,sizeof(int));
    }
    printf("enter the elements for mnatrix 1:\n");
    inputmatrix(mtr1,m,n);
    printf("enter the elements for mnatrix 2:\n");
    inputmatrix(mtr2,m,n);
    multiplication(mtr1,mtr2,mtrf,m,n);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%d\t",mtrf[i][j]);
        }
        printf("\n");
    }
    for(int i=0;i<m;i++)
    {
        free(mtr1[i]);
        free(mtr2[i]);
        free(mtrf[i]);
    }
    free (mtr1);
    free (mtr2);
    free (mtrf);
}