#include<stdio.h>
#include<math.h>
int main()
{
	float rate,time,principal,si,ci;
	printf("enter the principal, rate of interest, time in years\n");
	scanf("%f %f %f",&principal,&rate,&time);
	
	si=principal*rate*time/100;
	printf("simple interest is %f",si);
	
	ci=(principal*(pow((1+rate/100),time)))-principal;
	printf("compound interest is %f",ci);
	return 0;
	
	
	
	
	
}
