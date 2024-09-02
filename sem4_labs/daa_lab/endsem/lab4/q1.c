#include<stdio.h>
#include<stdlib.h>
int min(int**mat,int n)
{
    if(n==0)
    {
        return 0;
    }
    int smallest=1e9;
    int value;
    for(int i=0;i<n;i++)
    {
        value=mat[0][i];
        int **matrix=(int**)malloc((n-1)*sizeof(int*));
        for(int j=0;j<(n-1);j++)
        {
            matrix[j]=(int*)malloc((n-1)*sizeof(int));
        }
        int row=0,column=0;
        for(int k=1;k<n;k++)
        {
            column=0;
            for(int j=0;j<n;j++)
            {
                if(j==i)
                {
                    continue;
                }
                else
                {
                    matrix[row][column]=mat[k][j];
                    column++;
                }
            }
            row++;
        }
        value=value+min(matrix,n-1);
        if(value<smallest)
        {
            smallest=value;
        }
    }
    return smallest;
}
int main()
{
    int m;
    printf("Enter the value of m: ");
    scanf("%d", &m);
    int **mat = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) 
    {
        mat[i] = (int *)malloc(m * sizeof(int));
    }
    printf("Enter the values of the matrix:\n");
    for (int i = 0; i < m; i++) 
    {
        for (int j = 0; j < m; j++) 
        {
            scanf("%d", &mat[i][j]);
        }
    }
    int r = min(mat,m);
    printf("best values is %d",r);
}