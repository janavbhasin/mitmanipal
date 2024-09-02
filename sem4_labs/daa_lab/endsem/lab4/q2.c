#include<stdio.h>
int stack[100],top=-1;
void push(int value)
{
    stack[++top]=value;
}
int pop()
{
    return stack[top--];
}
void dfs(int mat[4][4],int visited[4],int vertices,int startVertex)
{
    push(startVertex);
    visited[startVertex]=1;
    while(top!=-1)
    {
        int currentVertex=pop();
        int smallest=-1;
        printf("pushed %d\n",currentVertex);
        for(int i=0;i<vertices;i++)
        {
            if(visited[i]!=1 && mat[currentVertex][i]==1)
            {
                if(smallest==-1||smallest>i)
                {
                    smallest=i;
                }
            }
        }
        if(smallest!=-1)
        {
            visited[smallest]=1;
            printf("pushed %d\n",smallest);
            push(smallest);
        }
    }
}
int main()
{
    int vertices=4,startVertex=0,graph[4][4]={{0,1,1,1},{0,0,0,1},{0,0,0,0},{0,0,1,0}},visited[4] = {0};
    dfs(graph, visited, vertices, startVertex);
}