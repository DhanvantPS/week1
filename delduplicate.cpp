#include<stdio.h>
int len(array)
int main()
{
	
	int n,m,count,k;
	printf("no.of elements in array ");
	scanf("%d",&n);
	int arr[n];
	for (int i=0;i<n;i++)
	scanf("%d",&arr[i]);
	
	int a[n];
	
	for(int i=0;i,n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(arr[i]=a[j])
			{
				count++;
			}
		if(count==0)
		{
		a[len(a)]=arr[i];
	    }
		}
	
	}
	for (int i=0;i<len(a);i++)
	{
		printf("%d",a[i]);
	}
	
}

int len(ar)
{
	int count,i;
	for(i=0;ar[i]!='\0';i++)
	{
		count++;
	}
	return count;
}
