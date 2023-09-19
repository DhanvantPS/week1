#include<stdio.h>
int main()
{
	
	int a,b,c;
	printf("enter the sides of triangle\n ");
	scanf("%d %d %d",&a,&b,&c);
	if (a+b>c)
		if (a==b && b==c)
			printf("equilateral");
		else if (a==b || b==c)
			printf("isoceles");
		else
			printf("scalene");
				
	else
		printf("invalid input");
		
	return 0;
				
	
}
