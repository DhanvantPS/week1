#include<stdio.h>
int main()
{
	
	int n,m;
	printf("no.of elements ")
	scanf("%d",&n);
	int arr[n];
	printf("enter the elements\n")
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);	
	for(int i=0;i<n;i++)
	{
		for (int j=0;j<n-i-1;j++)	
		{
			if (arr[j]<arr[j+1])
			{
				m=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=m;
			}		
		}		
	}
	
	for(int i=0;i<n;i++)
	{
		printf("%d",arr[i]);
		
	}
}
