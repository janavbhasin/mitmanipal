#include<stdio.h>
#include<string.h>
int palindrome(char str[],int index,int length)
{
    if(index<length)
    {
        if(str[length-index-1]==str[index])
        {
            palindrome(str,index+1,length);
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 1;
    }
}
int main()
{
    char str[20];
    scanf("%s",str);
    int i=palindrome(str,0,strlen(str));
    if(i==0)
    {
        printf("its not a palindrome");
    }
    else if(i==1)
    {
        printf("its a palindrome");
    }
}