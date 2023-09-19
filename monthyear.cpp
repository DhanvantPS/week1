#include <stdio.h>
int main()
{
	int yr,mth;
	printf("enter year and month\n");
	scanf("%d %d",&yr,&mth);
	if ((mth>=1 && mth<=12) && yr>0)
	{
		if (yr%4==0 && (yr%400==0 || yr%100!=0))
		{
			if (mth==(4,6,9,11))
			{
				printf("30");
		 	}
			else if (mth==2)
			{
				printf("29");
			}
			else
			{
				printf("31");
			}
		}
		else
		{
			if (mth==(4,6,9,11))
				printf("30");
			else if (mth==2)
				printf("28");
			else
			{
				printf("31");
			}
		}
	}
	else
	printf("invalid input");
	
	
}
