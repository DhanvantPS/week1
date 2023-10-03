#include<stdio.h>
int main()
{
	int i,j,k;
	for(i=0;i<=4;i++)
	{
		for(j=0;j<=i;j++)
		{
			printf("* ");
		}
		for(k=1;k<=8-2*i;k++)
		{
			printf("  ");
		}
		for(int l=0;l<=i;l++)
		{
			printf("* ");
		}
		printf("\n");
		
	}	
	
	for(i=0;i<=4;i++)
	{
		for(j=4;j>=i;j--)
		{
			printf("* ");
		}
		for(k=1;k<=2*i;k++)
		{
			printf("  ");
		}
		for(int l=4;l>=i;l--)
		{
			printf("* ");
		}
		printf("\n");
	}
	
	
}
