#include<stdio.h>
int main()
{
	int a,b,c;
	printf("enter the three numbers\n");
	scanf("%d %d %d",&a,&b,&c);
	if (a>=b && b>=c)
		{
			printf("%d is the greatest",a);
		}
	else if (b>=a && b>=c)
		{
			printf("%d is the greatest",b);
		}
	else
		{
			printf("%d is the greatest",c);
		}
	return 0;
}
