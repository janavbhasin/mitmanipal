#include<stdio.h>
int tower_of_hanoi(int n,char source,char dest,char aux)
{
    static int c=0;
    if(n==1)
    {
        printf("move disk 1 from %c to %c\n",source,dest);
        c++;
    }
    else
    {
        tower_of_hanoi(n-1,source,aux,dest);
        printf("move disk %d from %c to %c\n",n,source,dest);
        c++;
        tower_of_hanoi(n-1,aux,dest,source);
    }
    return c;
}
int main()
{
    int a=tower_of_hanoi(4,'a','b','c');
    printf("%d",a);
}