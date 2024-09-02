#include<stdio.h>
void copy(char str[],char str_copy[],int index)
{
    if (str[index]=='\0')
    {
        str_copy[index]='\0';
        return;
    }
    else
    {
        str_copy[index]=str[index];
        copy(str,str_copy,index+1);
    }
}
int main()
{
    char str[10],str_copy[10];
    int index=0;
    printf("enter the string ");
    scanf("%s",str);
    copy(str,str_copy,index);
    printf("copied string is\n");
    printf("%s",str_copy);
}