#include<stdio.h>
#include<string.h>
int palindrome(char str[],int ind,int len)
{
    if(ind<len)
    {
        if(str[len-ind-1]==str[ind])
        {
            palindrome(str,ind+1,len);
        }
        else
        {
            return 0;
        }
    }
    return 1;
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