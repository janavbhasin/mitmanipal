#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    int val;
    struct Node*l;
    struct Node*r;
}Node;

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
        printf("%d entered to left node",val);
    }
    else if(direct==2)
    {
        parent->r=newnode;
        printf("%d entered to right node",val);
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
            printf("enter vale to be entered\n");
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
                printf("already at root");
            }
            else
            {
                iter=prev;
                printf("move up to root %d",iter->val);
            }
        }
    }while(inp!=4);
}

void iterativepreorder(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    Node *stack[100];
    int top = -1;
    stack[++top] = root;

    while (top >= 0)
    {
        Node *node = stack[top--];
        printf("%d\t", node->val);

        if (node->r != NULL)
        {
            stack[++top] = node->r;
        }
        if (node->l != NULL)
        {
            stack[++top] = node->l;
        }
    }
}

void iterativepostorder(Node*root)
{
    if(root==NULL)
    {
        return;
    }
    Node*stack[100];
    int top=-1;
    Node*prev=NULL;
    do
    {
        while(root!=NULL)
        {
            stack[++top]=root;
            root=root->l;
        }
        while(top!=-1&&root==NULL)
        {
            Node*temp=stack[top];
            if(temp->r==NULL||temp->r==prev)
            {
                printf("%d\t",temp->val);
                top--;
                prev=temp;
            }
            else
            {
                root=temp->r;
            }
        }
    }while(top!=-1);
    return;
}
void iterativeinorder(Node*root)
{
    if(root==NULL)
    {
        return;
    }
    Node*stack[100];
    int top=-1;
    while(root!=NULL||top!=-1)
    {
        while(root!=NULL)
        {
            stack[++top]=root;  
            root=root->l;
        }

        root=stack[top--];
        printf("%d\t",root->val);

        root=root->r;
    }
}

void levelorder(Node*root)
{
    if(root==NULL)
    {
        return;
    }

    Node*queue[100];
    int front=0,rear=-1;
    queue[++rear]=root;

    while(front<=rear)
    {
        Node*node=queue[front++];
        printf("%d\t",node->val);
        if(node->l!=NULL)
        {
            queue[++rear]=node->l;
        }
        if(node->r!=NULL)
        {
            queue[++rear]=node->r;
        }
    }
}

int main()
{
    Node*tree=NULL;
    createbt(&tree);
    printf("inorder:\n");
    iterativeinorder(tree);
    printf("\npostorder:\n");
    iterativepostorder(tree);
    printf("\npreorder:\n");
    iterativepreorder(tree);  
    printf("\nlevelorder:\n");
    levelorder(tree);          
}