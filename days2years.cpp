#include<stdio.h>
int main()
{
	float days;
	char leap;
	float year;
	printf("if it is a leap year y or n ");
	scanf("%c",&leap);
	scanf("%f",&days);
	if (leap=='y')
		{
			year=(days/366);
			printf("days to years is %f ",year);
		}
	else if (leap='n')
		{
			year=(days/365);
			printf("days to years is %f ",year);
		}
	else
		{
			printf("invalid");
		}	
	return 0;
}


