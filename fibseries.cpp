#include<stdio.h>
int main()
{
	int n,a,b,s;
	a=0;
	b=1;
	s=0;
	printf("enter the number ");
	scanf("%d",&n);
	
	if (n!=1)
		
		{
			for(int i=1;i<n-1;i++)	
			{
				s=a+b;
				a=b;	
				b=s;		
			}
			printf("%d term of fib series is %d",n,b);
		}
	else
		printf("1st term of fib series is %d",0);
	
	return 0;
	
}
