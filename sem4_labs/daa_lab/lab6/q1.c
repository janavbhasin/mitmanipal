#include <stdio.h>
#include <stdlib.h>
int vertices=0;
typedef struct node 
{
    int val;
    struct node *l;
    struct node *r;
} node;
node *newnode(int value) 
{
    node *new = (node *)malloc(sizeof(node));
    new->val = value;
    new->l = NULL;
    new->r = NULL;
    return new;
}
node *leftright(int direct, int val, node *root) 
{
    node *new = newnode(val);
    if (direct == 1) 
    {
        root->l = new;
    } 
    else if (direct == 2) 
    {
        root->r = new;
    }
    return root;
}
void preorder_traversal(node *root) 
{
    if (root != NULL) 
    {
        vertices++;
        preorder_traversal(root->l); 
        preorder_traversal(root->r); 
    }
}
int main() 
{
    node *root = newnode(1);
    leftright(1, 2, root);
    leftright(2, 3, root);
    leftright(1, 4, root->l);
    leftright(2, 5, root->l);    
    preorder_traversal(root);
    printf("the no of nodes are %d\n",vertices);
}