#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX_SIZE 100
typedef enum 
{
    lparan,
    rparan,
    plus,
    minus,
    multiply,
    divide,
    eos,
    modulus,
    operand
}PRECEDENCE;
int stack[MAX_SIZE];
char expr[MAX_SIZE];
int pop(int*top)
{
    int x=stack[*top];
    *top=*top-1;
    return x;
}
void push(int *top,int x)
{
    *top=*top+1;
    stack[*top]=x;
}
PRECEDENCE get_token(char *symbol,int*n)
{
    *symbol=expr[(*n)];
    *n=*n+1;
    switch(*symbol)
    {
        case'+':
        return plus;
        case'-':
        return minus;
        case'/':
        return divide;
        case'*':
        return multiply;
        case'\0':
        return eos;
        case'%':
        return modulus;
        case'(':
        return lparan;
        case')':
        return rparan;
        default:
        return operand;
    }
}
int eval()
{
    char symbol;
    int n=0,top=-1,op1,op2,c;
    PRECEDENCE token=get_token(&symbol,&n);
    while(token!=eos)
    {
        if(token==operand)
        {
            c=symbol-'0';
            push(&top,c);
        }
        else
        {
            op1=pop(&top);
            op2=pop(&top);
            if(token==plus)
            {
                push(&top,op2+op1);
            }
            else if(token==minus)
            {
                push(&top,op2-op1);
            }
            else if(token==divide)
            {
                push(&top,op2/op1);
            }
            else if(token==multiply)
            {
                push(&top,op2*op1);
            }
            else if(token==modulus)
            {
                push(&top,op2%op1);
            }
        }
        token=get_token(&symbol,&n);
    }
    return pop(&top);
}
int main()
{
    char exp[100];
    printf("write the expression");
    scanf("%s",expr);
    printf("%d",eval());
}