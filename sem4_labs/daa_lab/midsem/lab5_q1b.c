#include<stdio.h>
int size;
void topologicalsort(int graph[size][size])
{
    int flag=0;
    int indegree[size],removed[size];
    while(flag!=size)
    {
        for(int i=0;i<size;i++)
        {
            indegree[i]=0;
            for(int j=0;j<size;j++)
            {
                if(graph[j][i]==1)
                {
                    indegree[i]++;
                }
            }
        }
        int k;
        for(int i=0;i<size;i++)
        {
            if(indegree[i]==0 && removed[i]!=-1)
            {
                removed[i]=-1;
                printf("%d\t",i);
                k=i;
                break;
            }
        }
        for(int i=0;i<size;i++)
        {
            graph[k][i]=0;
        }
        flag++;
    }
}
int main() {
    size = 7;
    int graph[7][7] = {{0, 1, 1, 0, 0, 0, 0},{0, 0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 1, 0}, {1, 1, 1, 0, 0, 1, 1},{0, 0, 0, 0, 0, 0, 0},{0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 0}};
    printf("Topological Sorting Order: ");
    topologicalsort(graph);
}