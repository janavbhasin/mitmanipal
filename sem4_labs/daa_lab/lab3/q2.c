#include <stdio.h>
#include <string.h>
int main()
{
	char a[20],b[20];
	int i,j=0,op=0,x=0;
	printf("enter the big string:\n");
	scanf("%s",a);
	printf("enter the small string:\n");
	scanf("%s",b);
	int n=strlen(a),m=strlen(b);
	for(i=0;i<n-m;i++)
	{
		op++;
		while(j<m)
		{
			if(a[i+j]==b[j])
			{
				op++;
				j++;
				if(j==m)
				{
					x=1;
				}
			}
			else
			{
				break;
			}
		}
		if(x==1)
		{
			break;
		}
	}
	if(x==1)
	{
		printf("key found\n");
	}
	else
	{
		printf("key not found\n");
	}
	printf("opcount is %d\n",op);
}