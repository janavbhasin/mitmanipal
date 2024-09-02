#include<stdio.h>
#include<ctype.h>
char stack[20];
int top=-1;
void push(char x)
{
    stack[++top]=x;
}
char pop()
{
    if (top==-1)
    {
        return -1;
    }
    else
    {
        return stack[top--];
    }
}
int priority(char x)
{
    if(x=='(')
    {
        return 0;
    }
    else if(x=='+'||x=='-')
    {
        return 1;
    }
    else if(x=='*'||x=='/')
    {
        return 2;
    }
    return -1;
}
int main()
{
    char exp[20];
    char *e,x;
    printf("Enter the expression");
    scanf("%s",exp);
    e=exp;
    while(isdigit(*e))
    {
        if(*e>=0||*e<=9)
        {
            printf("%c",*e);
        }
        else if(*e=='(')
        {
            push(*e);
        }
        else if(*e==')')
        {
            while((x=pop())!='(')
            {
                printf("%c",pop());
            }
            push(*e);
        }
        else 
        {
            while (top != -1 && priority(stack[top]) >= priority(*e)) 
            {
                printf("%c", pop());
            }
        e++;
        }
    }
    while(top!=-1)
    {
        printf("%c",pop());
    }
}