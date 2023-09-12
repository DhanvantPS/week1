#include<stdio.h>
int main()
{
	float a,b;
	int c;
	scanf("%f %f",&a,&b);
	printf("float product is %f\n",a*b);
	c=a*b;
	c=(int)c;
	printf("int product is %d",c);
	return 0;
}
