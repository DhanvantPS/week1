#include<stdio.h>
int main()
{
	float percentage,a,b,c,d,e,total;
	printf("enter the all the 5 marks ");
	scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
	printf("enter the total mark of the test ");
	scanf("%d",&total);
	total=((a+b+c+d+e)/5)/total;
	percentage=total*100;
	printf("your percentage is %f",percentage);
	return 0;
	
}
