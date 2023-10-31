#include<stdio.h>
int main()
{
	
	int n,m,count,k;
	printf("no.of elements in array ");
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);

	printf("k value is ");
	scanf("%d",&k);
	
	for(int i=0;i<n;i++)
	{
		if(arr[i]==k)
		{
			count++;
		}
		
	}
	printf("no.of times k appeared is %d",count);
}
