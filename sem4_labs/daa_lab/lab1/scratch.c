#include <stdio.h>
#include <stdlib.h>

// Node structure for the linked list
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int vertex) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

// Function to add an edge to the adjacency list
void addEdge(Node* adjacencyList[], int src, int dest) {
    Node* newNode = createNode(dest);
    newNode->next = adjacencyList[src];
    adjacencyList[src] = newNode;

    newNode = createNode(src);
    newNode->next = adjacencyList[dest];
    adjacencyList[dest] = newNode;
}

// Function to print the adjacency list
void printAdjacencyList(Node* adjacencyList[], int n) {
    printf("\nAdjacency List:\n");
    for (int i = 0; i < n; i++) {
        printf("Adjacents of vertex %d: ", (i + 1));
        Node* current = adjacencyList[i];
        while (current != NULL) {
            printf("%d ", current->vertex + 1);
            current = current->next;
        }
        printf("\n");
    }
}

// Function to print the adjacency matrix
void printAdjacencyMatrix(Node* adjacencyList[], int n) {
    printf("\nAdjacency Matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int connected = 0;
            Node* current = adjacencyList[i];
            while (current != NULL) {
                if (current->vertex == j) {
                    connected = 1;
                    break;
                }
                current = current->next;
            }
            printf("%d\t", connected);
        }
        printf("\n");
    }
}

int main() {
    int n, i, j, x;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    // Creating an array of pointers to Node to represent the adjacency list
    Node* adjacencyList[n];
    for (i = 0; i < n; i++) {
        adjacencyList[i] = NULL;
    }

    // Building the adjacency list
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            printf("Are %d and %d connected? 1 for yes, 0 for no: ", (i + 1), (j + 1));
            scanf("%d", &x);

            if (x == 1) {
                addEdge(adjacencyList, i, j);
            }
        }
    }

    // Printing the adjacency list
    printAdjacencyList(adjacencyList, n);

    // Printing the adjacency matrix
    printAdjacencyMatrix(adjacencyList, n);

    return 0;
}
