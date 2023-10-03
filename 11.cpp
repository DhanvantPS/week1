#include<stdio.h>
int main()
{
	int i,j,k;
	for(i=1;i<=5;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("  ");
		}
		for(k=5;k>=i;k--)
		{
			printf("* ");
		}
		printf("\n");		
	}
	int p,q,r;
	for(p=1;p<=5;p++)
	{
		for(q=5;q>=p;q--)
		{
			printf("  ");
		}
		for(r=1;r<=p;r++)
		{
			printf("* ");
		}
		printf("\n");		
	}
	
	
	
}
	
	

