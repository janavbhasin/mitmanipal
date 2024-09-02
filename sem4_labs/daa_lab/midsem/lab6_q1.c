#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    struct node*l;
    struct node*r;
    int val;
}Node;
Node*newnode(int value)
{
    Node*new=(Node*)malloc(sizeof(Node));
    new->l=new->r=NULL;
    new->val=value;
    return new;
}
void insert(Node*parent,int direct,int value)
{
    Node*new=newnode(value);
    if(direct==1)
    {
        parent->l=new;
    }
    else if(direct==2)
    {
        parent->r=new;
    }
}
int nodes=0;
void inorder(Node*tree)
{
    if(tree==NULL)
    {
        return ;
    }
    inorder(tree->l);
    nodes++;
    inorder(tree->r);
}
void createbt(Node**tree)
{
    int x ,inp;
    printf("enter the value of the root\n");
    scanf("%d",&x);
    *tree=newnode(x);
    Node*iter=*tree;
    Node*prev=NULL;
    do
    {
        printf("\n1 for left\n2 for right\n3 to move up\n4 for exit\n");
        scanf("%d",&inp);
        if(inp==1||inp==2)
        {
            printf("enter the value\n");
            scanf("%d",&x);
            insert(iter,inp,x);
            prev=iter;
            if(inp==1)
            {
                iter=iter->l;
            }
            else if(inp==2)
            {
                iter=iter->r;
            }
        }
        else if(inp==3)
        {
            if(iter==*tree)
            {
                printf("already at root\n");
            }
            else
            {
                iter=prev;
                printf("moved up to %d",iter->val);
            }
        }
    }while(inp!=4);
}
int main()
{
    Node*tree=(Node*)malloc(sizeof(Node));
    createbt(&tree);
    inorder(tree);
    printf("no of nodes are %d\n",nodes);
}