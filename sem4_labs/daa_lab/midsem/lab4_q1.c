#include<stdio.h>
#include<stdlib.h>
int min(int **mat,int m)
{
    if(m==0)
    {
        return 0;
    }
    int value,smallest=1e9;
    for(int i=0;i<m;i++)
    {
        value=mat[0][i];
        int **matrix=(int**)malloc((m-1)*sizeof(int*));
        for(int k=0;k<m-1;k++)
        {
            matrix[k]=(int*)malloc((m-1)*sizeof(int));
        }
        int row=0,column=0;
        for(int k=1;k<m;k++)
        {
            column=0;
            for(int j=0;j<m;j++)
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
        value=value+min(matrix,m-1);
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