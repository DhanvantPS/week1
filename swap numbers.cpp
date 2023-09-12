#include<stdio.h>
int main()

{
	int a,b,c;
	printf("A is ");
	scanf("%d",&a);
	printf("B is ");
	scanf("%d",&b);
	c=a;
	a=b;
	b=c;
	printf("A is %d and B is %d",a,b);
	return 0;
	
	
}
