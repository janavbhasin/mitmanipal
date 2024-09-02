#include<stdio.h>
#include<stdlib.h>
struct dob
    {
        int day;
        int *month;
        int year;
    };
struct stu_info
    {
        int reg_no;
        char * name;
        char adress[100];
    };
struct college
    {
        char * clg_name;
        char uni_name[100];
    };
typedef struct 
{
    struct dob *dmy;
    struct stu_info stu;
    struct college clg;
}student;
void read(student*ptr)
{
    printf("enter date of birth: ");
    scanf("%d%d%d",&(ptr->dmy->day),ptr->dmy->month,&(ptr->dmy->year));
    printf("enter reg no.: ");
    scanf("%d",&ptr->stu.reg_no);
    printf("enter name: ");
    scanf("%s",ptr->stu.name);
    printf("enter adress: ");
    scanf("%s",ptr->stu.adress);
    printf("enter college name: ");
    scanf("%s",ptr->clg.clg_name);
    printf("enter university name: ");
    scanf("%s",ptr->clg.uni_name);
}
void display(student*ptr)
{
    printf("the student name is: %s\n",ptr->stu.name);
    printf("student registration number is: %d\n",ptr->stu.reg_no);
    printf("student date of birth is: %d/%d/%d\n",ptr->dmy->day,*(ptr->dmy->month),ptr->dmy->year);
    printf("student adress is: %s\n",ptr->stu.adress);
    printf("student college name: %s\n",ptr->clg.clg_name);
    printf("student university name is: %s\n",ptr->clg.uni_name);
}
int main()
{
    int n;
    printf("enter the no of students: ");
    scanf("%d",&n);
    printf("\n");
    student*ptr=(student*)calloc(n,sizeof(student));
    for(int i=0;i<n;i++)
    {
        (ptr+i)->dmy=(struct dob*)calloc(n,sizeof(struct dob));
        (ptr+i)->dmy->month=(int *)calloc(n,sizeof(int));
        (ptr+i)->stu.name=(char*)calloc(n,sizeof(char));
        (ptr+i)->clg.clg_name=(char*)calloc(n,sizeof(char));
    }
    ptr->dmy=(struct dob*)calloc(n,sizeof(struct dob));
    ptr->dmy->month=(int *)calloc(n,sizeof(int));
    ptr->stu.name=(char*)calloc(n,sizeof(char));
    ptr->clg.clg_name=(char*)calloc(n,sizeof(char));
    for(int i=0;i<n;i++)
    {
        read(ptr+i);
        printf("\n");
    }
    for(int i=0;i<n;i++)
    {
        display(ptr+i);
        printf("\n");
    }
}