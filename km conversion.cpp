#include<stdio.h>
int main()
{
	int dist;
	printf("enter the distance in km ",&dist);
	scanf("%d",&dist);
	printf("distance in meter is %ld\n",dist*1000);
	printf("distance in centimeter is %ld\n",dist*100000);
	printf("distance in millimeter is %ld",dist*1000000);
	return 0;
	
}
