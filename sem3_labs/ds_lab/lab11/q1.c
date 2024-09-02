#include <stdio.h>
#include <stdlib.h>
#include "functions.h"

int main()
{
    Node *tree = (Node *)malloc(sizeof(Node));
    createbt(&tree);
    printf("Inorder:\n");
    inorder(tree);
    printf("\nPre Order:\n");
    preorder(tree);
    printf("\nPost Order:\n");
    postorder(tree);
    printf("\n");
}