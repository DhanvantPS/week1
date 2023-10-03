#include<stdio.h>
int main()
{
	int i,j,k;
	for(i=0;i<=4;i++)
	{
		for(j=0;j<i;j++)
		{
	 		printf("  ");	
		}		
		for(k=9;k>=2*i+1;k=k-1)
		{
			printf("* ");
		}
		printf("\n");
	}
	
	
}
