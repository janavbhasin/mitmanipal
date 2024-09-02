#include <stdio.h>
#include <string.h>

#define stacksize 100
#define exprsize 100

int stack[stacksize];
char expr[exprsize];

void push(int *top, int x) {
    *top = *top + 1;
    stack[*top] = x;
}

int pop(int *top) {
    int item = stack[*top];
    *top = *top - 1;
    return item;
}

typedef enum {
    lparan,
    rparan,
    minus,
    plus,
    modulus,
    eos,
    operand,
    multiply,
    divide
} PRECEDENCE;

PRECEDENCE get_token(char *symbol, int *n) {
    *symbol = expr[(*n)++];
    switch (*symbol) {
        case '+':
            return plus;
        case '-':
            return minus;
        case '/':
            return divide;
        case '*':
            return multiply;
        case '\0':
            return eos;
        case '%':
            return modulus;
        case '(':
            return lparan;
        case ')':
            return rparan;
        default:
            return operand;
    }
}

int eval() {
    char symbol;
    int n = 0, top = -1;
    int op1, op2, c;
    PRECEDENCE token = get_token(&symbol, &n);
    while (token != eos) {
        if (token == operand) {
            c = symbol - '0';
            push(&top, c);
        } else {
            op1 = pop(&top);
            op2 = pop(&top);
            if (token == plus) {
                push(&top, op2 + op1);
            } else if (token == minus) {
                push(&top, op2 - op1);
            } else if (token == divide) {
                push(&top, op2 / op1);
            } else if (token == multiply) {
                push(&top, op2 * op1);
            } else if (token == modulus) {
                push(&top, op2 % op1);
            }
        }
        token = get_token(&symbol, &n);
    }
    return pop(&top);
}

int main() {
    printf("Enter the expression: ");
    scanf("%s", expr);
    printf("Result: %d\n", eval());
    return 0;
}
