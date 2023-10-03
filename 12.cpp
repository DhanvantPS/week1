#include<stdio.h>
int main()
{
	int i,j;
	for(i=1;i<=5;i++)
	{
		for(j=5;j>=i;j--)
		{
			printf("* ");
		}
		printf("\n");
	}

	int p,q;
	for(p=1;p<=5;p++)
	{
		for(q=1;q<=p;q++)
		{
			printf("* ");
		}
		printf("\n");		
	}
	
	
	
}
