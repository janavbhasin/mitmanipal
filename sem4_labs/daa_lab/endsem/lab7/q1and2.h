#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
    int val;
    int height;
    struct Node*l;
    struct Node*r;
}Node;
Node*newnode(int value)
{
    Node*node=(Node*)malloc(sizeof(Node));
    node->l=NULL;
    node->r=NULL;
    node->val=value;
    node->height=1;
    return node;
}
int height(Node*node)
{
    if(node==NULL)
    {
        return 0;
    }
    return node->height;
}
int max(int a,int b)
{
    if(a>b)
    {
        return a;
    }
    return b;
}
int balancefactor(Node*node)
{
    if(node==NULL)
    {
        return 0;
    }
    return height(node->l)-height(node->r);
}
Node*rightrotate(Node*root)
{
    Node*left=root->l;
    Node*t=left->r;
    left->r=root;
    root->l=t;
    root->height=max(height(root->l),height(root->r))+1;
    left->height=max(height(left->l),height(left->r))+1;
    return left;
}
Node*leftrotate(Node*root)
{
    Node*right=root->r;
    Node*t=right->l;
    right->l=root;
    root->r=t;
    root->height=max(height(root->l),height(root->r))+1;
    right->height=max(height(right->l),height(right->r))+1;
    return right;
}
Node*insert(Node*root,int value)
{
    if(root==NULL)
    {
        return newnode(value);
    }
    else
    {
        if(value<root->val)
        {
            root->l=insert(root->l,value);
        }
        else if(value>root->val)
        {
            root->r=insert(root->r,value);
        }
        else
        {
            return root;
        }
    }
    root->height=max(height(root->l),height(root->r))+1;
    int balance= balancefactor(root);
    if(balance>1 && value<root->l->val)
    {
        return rightrotate(root);
    }
    if(balance<-1 && value>root->r->val)
    {
        return leftrotate(root);
    }
    if(balance>1 && value>root->l->val)
    {
        root->l=leftrotate(root->l);
        return rightrotate(root);
    }
    if(balance<-1 && value<root->r->val)
    {
        root->r=rightrotate(root->r);
        return leftrotate(root);
    }
    return root;
}
void preorder(Node*root)
{
	if(root==NULL)
	{
		return;
	}
	printf("%d ",root->val );
	preorder(root->l);
	preorder(root->r);
}
void predeccesor(Node*root,int want)
{
    if (root->l->val==want||root->r->val==want)
    {
        printf("\n%d\n",root->val);
        return;
    }
    else if(root->val>want)
    {
        predeccesor(root->l,want);
    }
    else
    {
        predeccesor(root->r,want);
    }
}
void succesor(Node*root,int want)
{
    if(root==NULL)
    {
        return;
    }
    if(root->val==want)
    {
        if(root->l!=NULL)
        {
            printf("%d\n",root->l->val);
        }
        if(root->r!=NULL)
        {
            printf("%d\n",root->r->val);
        }
        return;
    }
    else if(root->val>want)
    {
        succesor(root->l,want);
    }
    else
    {
        succesor(root->r,want);
    }
}