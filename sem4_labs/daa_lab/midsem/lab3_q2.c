#include<stdio.h>
#include<string.h>
int main()
{
    char str1[100],str2[100];
    printf("enter the large string\n");
    scanf("%s",str1);
    printf("enter the small string\n");
    scanf("%s",str2);
    int j=0,flag=0,m=strlen(str1),n=strlen(str2);
    for(int i=0;i<(m-n);i++)
    {
        while(j<n)
        {
            if(str1[i+j]==str2[j])
            {
                j++;
            }
            else
            {
                break;
            }
        }
        if(j==n)
        {
            flag=1;
            break;
        }
        j=0;
    }
    if(flag==1)
    {
        printf("string matched\n");
    }
    else
    {
        printf("string not matched\n");
    }
}