#include<stdio.h>
int main()
{
	
	int n,total;
	printf("no.of elements in array ");
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);

	for(int i=0;i<n;i++)
	{
		total=total+arr[i];	
	}
	if((n*(n+1)/2)-total==0)
	printf("there is no missing element");
	
	else
	printf("the missing element is %d",(n*(n+1)/2)-total);
}


