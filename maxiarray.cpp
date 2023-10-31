#include<stdio.h>
int main()
{
	
	int n,m;
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);
	m=arr[0];
	for (int i=0;i<n;i++)
	{
		if (arr[i]>m)
		m=arr[i];
	}
	printf("\n%d",m);
	return 0;
}
