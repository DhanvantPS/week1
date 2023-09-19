#include<stdio.h>
int main()
{
	int n,p;
	p=1;
	printf("enter the number ");
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
 		p=p*i;
	
	printf("factorial is %d ",p);
	return 0;	
}
