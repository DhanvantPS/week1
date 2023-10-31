#include<stdio.h>
int main()
{
	
	int n,m;
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);
	
	
	if(n%2==0)
	{
		for(int i=0;i<(n+1)/2;i++)
		{
			m=arr[i];
			arr[i]=arr[n-i-1];
			arr[n-i-1]=m;
		
		}
	
	}	
	
	else if(n%2!=0)
	{
		for(int i=0;i<n/2;i++)
		{
			m=arr[i];
			arr[i]=arr[n-i-1];
			arr[n-i-1]=m;
		}
	}
	
	for(int i=0;i<n;i++)
	{
		printf("%d",arr[i]);
		
	}
	return 0;	
}
