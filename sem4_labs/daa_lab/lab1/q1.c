#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
    struct node*l;
    struct node*r;
    int val;
}Node;
Node*insertelement(Node*root,int value)
{
    Node* newnode = (Node*)malloc(sizeof(Node));
    newnode->l = newnode->r = NULL;
    newnode->val = value;
    return newnode;
}
void search(Node*root,int key)
{
    if(root->val==key)
    {
        printf("key found\n");
        return;
    }
    else if(root->val>key)
    {
        if(root->l==NULL)
        {
            root->l=insertelement(root,key);
            printf("entered the element to the left of %d",root->val);
            return;
        }
        else
        {
            search(root->l,key);
        }
    }
    else if(root->val<key)
    {
        if(root->r==NULL)
        {
            root->r=insertelement(root,key);
            printf("entered the element to the right of %d",root->val);
            return;
        }
        else
        {
            search(root->r,key);
        }
    }
}
void inorder(Node *p)
{
	if(p == NULL)
    {
		return;
    }
    else
    {
        inorder(p->l);
        printf("%d \t",p->val);
        inorder(p->r);
    }
}
void preorder(Node *p)
{
	if(p==NULL)
    {
        return;
    }
    else
	{
		printf("%d \t",p->val);
		preorder(p->l);
		preorder(p->r);
	}
}
void postorder(Node *p)
{
	if(p==NULL)
    {
        return;
    }
    else
	{
		postorder(p->l);
		postorder(p->r);
		printf("%d \t",p->val);
	}
}
int main()
{
    Node*root=(Node*)malloc(sizeof(Node));
    root->l=root->r=NULL;
    int x,value,ch=1;
    printf("enter the value of the root\n");
    scanf("%d",&x);
    root->val=x;
    Node*temp=root;
    while(ch!=5)
    {
        printf("\nenter \n1 for search,entry\n2 for inorder\n3 for preorder\n4 for postorder\n5 for quit\n");
        scanf("%d",&ch);
        if(ch==1)
        {
            root=temp;
            printf("enter the value to be searched or entered in the bst\n");
            scanf("%d",&value);
            search(root,value);
        }
        else if(ch==2)
        {
            inorder(root);
        }
        else if(ch==3)
        {
            preorder(root);
        }
        else if(ch==4)
        {
            postorder(root);
        }
        else if(ch==5)
        {
            printf("bye bye\n");
        }
    }
}