#include <stdio.h>

typedef struct
{
    int a[100];
    int tos;
} stack;

stack push(stack s, int x)
{
    s.tos++;
    s.a[s.tos] = x;
    return s;
}

long convert(stack s)
{
    long n = 0;
    for (int i = s.tos; i >= 0; i--)
    {
        n = n * 10 + s.a[i];
    }
    return n;
}

int main()
{
    stack s;
    s.tos = -1;
    int n, i;
    double num, dn;
    printf("Enter a decimal number ");
    scanf("%lf", &num);
    n = (int)num;
    while (n > 0)
    {
        s = push(s, (n % 2));
        n = n / 2;
    }
    long bin;
    bin = convert(s);
    printf("%ld",bin);
    return 0;
}