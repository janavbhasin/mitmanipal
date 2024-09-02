#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    char val;
    struct Node*l;
    struct Node*r;
}Node;

Node*createnode(char x)
{
    Node*newnode=(Node*)malloc(sizeof(Node));
    newnode->l=NULL;
    newnode->r=NULL;
    newnode->val=x;
    return newnode;
}

double eval(char c,double x,double y)
{
    if (c=='*')
    {
        return x*y;
    }
    else if(c=='+')
    {
        return x+y;
    }
    else if(c=='/')
    {
        return x/y;
    }
    else if(c=='-')
    {
        return x-y;
    }
}

double evaluate(Node*node)
{
    if(node==NULL)
    {
        return 0;
    }
    else if(node->r==NULL||node->l==NULL)
    {
        return (double)(node->val -'0');
    }

    double x = evaluate(node->l);
    double y = evaluate(node->r);

    return eval(node->val,x,y);
}

int main()
{
    Node *root = createnode('*');   
    root->l = createnode('+');
    root->r = createnode('/');
    root->l->l = createnode('1');
    root->l->r = createnode('6');
    root->r->l = createnode('9');
    root->r->r = createnode('4');

    printf("Ans :  %lf\n", evaluate(root));
}