#include<stdio.h>
int main()
{
	int n,s;
	s=0;
	printf("enter the number ");
	scanf("%d",&n);
	while (n!=0)	
	{
		n=n/10;
		s=s+1;
	}
	printf("no of digits=%d",s);
	return 0;
	
}
