#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
typedef struct Node
{
    int val;
    struct Node*r;
    struct Node*l;
}Node;

Node*createnode(int x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->val=x;
    newnode->l=NULL;
    newnode->r=NULL;
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
    printf("enter value of root\n");
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
            printf("enter the value of node");
            scanf("%d",&x);
            insertnode(iter,x,inp);
            prev=iter;
            if(inp==1)
            {
                iter=iter->l;
            }
            else if(inp==2)
            {
                iter =iter->r;
            }
        }
        else if(inp==3)
        {
            if(iter==*tree)
            {
                printf("already at root");
            }
            else
            {
                iter=prev;
                printf("moved up to %d",iter->val);
            }
        }
    }while(inp!=4);
}

void inorder(Node *tree)
{
    if (tree != NULL)
    {
        inorder(tree->l);
        printf("%d ", tree->val);
        inorder(tree->r);
    }
}

bool check(Node*c1,Node*c2)
{
    if(c1 == NULL && c2 == NULL)
    {
        return true;
    }
    else if(c1!=NULL && c2!=NULL && c1->val==c2->val)
    {
        bool left=check(c1->l,c2->l);
        bool right=check(c1->r,c2->r);

        return left && right;
    }
    else
    {
        return false;
    }
}

Node*copy(Node*tree)
{
    if(tree==NULL)
    {
        return NULL;
    }
    Node *newnode = createnode(tree->val);

    newnode->l = copy(tree->l);
    newnode->r = copy(tree->r);
    return newnode;
}
int main()
{
    Node*tree=NULL;
    createbt(&tree);
    Node*copied=copy(tree);
    printf("inorder of original tree:");
    inorder(tree);
    printf("\ninorder of copied tree:");
    inorder(copied);
    Node*check1=NULL;
    Node*check2=NULL;
    printf("\nenter the first tree to be checked\n");
    createbt(&check1);
    printf("enter the second tree to be checked\n");
    createbt(&check2);
    bool a=check(check1,check2);
    if(a==true)
    {
        printf("its equal");
    }
    else
    {
        printf("its not equal");
    }
    inorder(check1);
    inorder(check2);
}