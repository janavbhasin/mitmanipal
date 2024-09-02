#include<stdio.h>
#include<stdlib.h>
typedef struct employee
{
    char name[100];
    struct dob
    {
        int date;
        int month;
        int year;
    }dmy;
    struct adress
    {
        int houseno;
        int zip;
        char state[100];
    }add;
}employee;
void read(employee*ptr)
{
    printf("enter the employee name:\n");
    scanf("%s",ptr->name);
    printf("enter the employee date of birth:\n");
    scanf("%d%d%d",&ptr->dmy.date,&ptr->dmy.month,&ptr->dmy.year);
    printf("enter the employee adress:\n");
    scanf("%d%d%s",&ptr->add.houseno,&ptr->add.zip,ptr->add.state);
}
void display(employee*ptr)
{
    printf("the employee name is: %s",ptr->name);
    printf("\nemployee date of birth is:%d/%d/%d\n",ptr->dmy.date,ptr->dmy.month,ptr->dmy.year);
    printf("employee adress is:\n%d\n%d\n%s\n",ptr->add.houseno,ptr->add.zip,ptr->add.state);
}
int main()
{
    int n;
    printf("enter the number of employees:");
    scanf("%d",&n);
    employee*ptr=(employee*)calloc(n,sizeof(employee));
    for(int i=0;i<n;i++)
    {
        read(ptr);
    }
    for(int i=0;i<n;i++)
    {
        display(ptr);
    }
}