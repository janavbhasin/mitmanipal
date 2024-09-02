#include<stdio.h>
#include<stdlib.h>
typedef struct student
{
    char name[100];
    int roll;
    float cgpa;
}student;
void read(student*ptr,int n)
{
    for(int i=0;i<n;i++)
    {
    printf("enter the student name:\n");
    scanf("%s",(ptr+i)->name);
    printf("enter the student roll no.:\n");
    scanf("%d",&(ptr+i)->roll);
    printf("enter the student cgpa:\n");
    scanf("%f",&(ptr+i)->cgpa);
    }
}
void sort(student*ptr,int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<n;k++)
            {
                if((ptr+i)->roll<(ptr+j)->roll)
                {
                    student t=*(ptr+i);
                    *(ptr+i)=*(ptr+j);
                    *(ptr+j)=t;
                }
            }
        }
    }
}
void display(student*ptr,int n)
{
    for(int i=0;i<n;i++)
    {
    printf("name:%s\n",(ptr+i)->name);
    printf("roll:%d\n",(ptr+i)->roll);
    printf("cgpa:%f\n",(ptr+i)->cgpa);
    }
}
int main()
{
    int n;
    printf("enter the number of students : ");
    scanf("%d",&n);
    student*ptr=(student*)calloc(n,sizeof(student));
    printf("\n");
    read(ptr,n);
    sort(ptr,n);
    printf("\n");
    display(ptr,n);
}