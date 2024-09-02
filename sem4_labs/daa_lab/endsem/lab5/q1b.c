#include<stdio.h>
#include<stdlib.h>
void topological_sort(int mat[7][7],int n)
{
    int flag=0,arr[n],k=0;
    int removed[7]={0};
    while(flag!=n)
    {
        for(int i=0;i<n;i++)
        {
            arr[i]=0;
            for(int j=0;j<n;j++)
            {
                arr[i]=arr[i]+mat[j][i];
            }
        }
        for(int i=0;i<n;i++)
        {
            if(arr[i]==0 && removed[i]!=1)
            {
                removed[i]=1;
                printf("%d",i);
                k=i;
                break;
            }
        }
        for(int i=0;i<n;i++)
        {
            mat[k][i]=0;
        }   
        flag++;
    }
}
int main() 
{
    int vertices = 7;
    int graph[7][7] = {{0, 1, 1, 0, 0, 0, 0},{0, 0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 1, 0}, {1, 1, 1, 0, 0, 1, 1},{0, 0, 0, 0, 0, 0, 0},{0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 0}};
    printf("Topological Sorting Order: ");
    topological_sort(graph, vertices);
}