#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int val;
    struct Node *l;
    struct Node *r;
} Node;

Node *createnode(int x)
{
    Node *newnode = (Node *)malloc(sizeof(Node));
    newnode->l = NULL;
    newnode->r = NULL;
    newnode->val = x;
    return newnode;
}

void insertnode(Node *parent, int val, int direct)
{
    Node *newnode = createnode(val);
    if (direct == 1)
    {
        parent->l = newnode;
        printf("%d entered to left\n", val);
    }
    else if (direct == 2)
    {
        parent->r = newnode;
        printf("%d entered to right\n", val);
    }
}

void inOrderTraversal(Node *root, int *arr, int *index)
{
    if (root == NULL)
    {
        return;
    }

    inOrderTraversal(root->l, arr, index);
    arr[(*index)++] = root->val;
    inOrderTraversal(root->r, arr, index);
}

void sortedArrayToBST(Node *root, int *arr, int *index)
{
    if (root == NULL)
    {
        return;
    }

    sortedArrayToBST(root->l, arr, index);
    root->val = arr[(*index)++];
    sortedArrayToBST(root->r, arr, index);
}

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

void convertToBST(Node *root)
{
    if (root == NULL)
    {
        return;
    }

    int arr[100];
    int index = 0;

    // Perform in-order traversal and store values in an array
    inOrderTraversal(root, arr, &index);

    // Sort the array
    qsort(arr, index, sizeof(int), compare);

    // Perform in-order traversal again and replace values with sorted values
    index = 0;
    sortedArrayToBST(root, arr, &index);
}

void printInOrder(Node *root)
{
    if (root != NULL)
    {
        printInOrder(root->l);
        printf("%d\t", root->val);
        printInOrder(root->r);
    }
}

void createbt(Node **tree)
{
    int x, inp;
    printf("enter the value of root\n");
    scanf("%d", &x);

    *tree = createnode(x);
    Node *iter = *tree;
    Node *prev = NULL;
    do
    {
        printf("\n1 for left\n2 for right\n3 to move up\n4 for exit\n");
        scanf("%d", &inp);
        if (inp == 1 || inp == 2)
        {
            printf("enter the value of node\n");
            scanf("%d", &x);
            insertnode(iter, x, inp);
            prev = iter;
            if (inp == 1)
            {
                iter = iter->l;
            }
            else if (inp == 2)
            {
                iter = iter->r;
            }
        }
        else if (inp == 3)
        {
            if (iter == *tree)
            {
                printf("already at root\n");
            }
            else
            {
                iter = prev;
                printf("moved up to %d", iter->val);
            }
        }
    } while (inp != 4);
}

int main()
{
    Node *tree = (Node *)malloc(sizeof(Node));
    createbt(&tree);

    printf("Binary Tree before conversion to Binary Search Tree:\n");
    printInOrder(tree);
    printf("\n");

    convertToBST(tree);

    printf("Binary Search Tree after conversion:\n");
    printInOrder(tree);
    printf("\n");

    return 0;
}
