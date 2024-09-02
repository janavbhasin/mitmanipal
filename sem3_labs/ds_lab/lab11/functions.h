#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int val;
    struct node*r;
    struct node*l;
}Node;

void inorder(Node*tree)
{
    if(tree!=NULL)
    {
        inorder(tree->l);
        printf("%d",tree->val);
        inorder(tree->r);
    }
}

void preorder(Node*tree)
{
    if(tree!=NULL)
    {
        printf("%d",tree->val);
        preorder(tree->l);
        preorder(tree->r);
    }
}

void postorder(Node*tree)
{
    if(tree!=NULL)
    {
        postorder(tree->l);
        postorder(tree->r);
        printf("%d",tree->val);
    }
}

Node*createnode(int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->l=NULL;
    newnode->r=NULL;
    newnode->val=x;
    return newnode;
}

void insertnode(Node*parent,int val,int direct)
{
    Node*newnode=createnode(val);
    if(direct==1)
    {
        parent->l=newnode;
        printf("%d entered to left\n",val);
    }
    else if(direct==2)
    {
        parent->r=newnode;
        printf("%d entered to right\n",val);
    }
}

void createbt(Node**tree)
{
    int x,inp;
    printf("enter the value of root\n");
    scanf("%d",&x);

    *tree=createnode(x);
    Node*iter=*tree;
    Node*prev=NULL;
    do
    {
        printf("\n1 for left\n2 for right\n3 to move up\n4 for exit\n");
        scanf("%d",&inp);
        if(inp==1||inp==2)
        {
            printf("enter the value of node\n");
            scanf("%d",&x);
            insertnode(iter,x,inp);
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
    } while (inp!=4);
}