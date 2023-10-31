#include<stdio.h>
int main()
{
	
	int n,m,k;
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);
	
	for(int i=0;i<n;i++)
	{
		for (int j=0;j<n-i-1;j++)	
		{
			if (arr[j]>arr[j+1])
			{
				m=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=m;
			}	
		}
			
	}
	
	printf("k value is ");
	scanf("%d",&k);
	printf("%d %d",arr[k-1],arr[n-k]);
	
}
