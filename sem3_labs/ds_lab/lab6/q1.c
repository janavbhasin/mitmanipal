#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define STACK_SIZE 20
#define EXPR_SIZE 20
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
int stack[STACK_SIZE];
char expr[EXPR_SIZE];
void push(int*top,int x)
{
    *top+=1;
    stack[*top]=x;
}
int pop(int *top)
{
    int temp=stack[*top];
    *top-=1;
    return temp;
}
PRECEDENCE get_token(char*symbol,int*n)
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
            op2=pop(&top);
            op1=pop(&top);
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
    scanf("%s",exp);
    for(int i=strlen(exp)-1,j=0;i>=0;i--,j++)
    {
        expr[j]=exp[i];
    }
    printf("%d",eval());
}