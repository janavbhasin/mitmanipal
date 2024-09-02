#include <stdio.h>
#include "q1.h"
int main() 
{
    Node *root = NULL;
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);
    printf("preorder traversal of the constructed AVL tree is \n");
    preorder(root);
    predecessor(root,40);
    successor(root,40);
}