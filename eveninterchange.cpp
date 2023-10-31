#include<stdio.h>
int main()
{
	
	int n,m;
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);
	
	if (n%2==0)
	{
		for(int i=0;i<n-1;i=i+2)
		{
			m=arr[i+1];
			arr[i+1]=arr[i];
			arr[i]=m;
		}
		
		
		
	}

		for(int i=0;i<n;i++)
	{
		printf("%d",arr[i]);
		
	}
	return 0;	
}


