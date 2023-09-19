#include<stdio.h>
int main()
{
	 float surcharge,units;
	printf("enter the units of current ");
	scanf("%f",&units);
	printf("enter the surcharge of current ");
	scanf("%f",&surcharge);
	
	printf("your electricity bill is %f",units*8+surcharge);
	return 0;
	
}
