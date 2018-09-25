#include<stdio.h>
int partition(int a[],int start,int end)
{
    int pivot=a[end],pindex=start,temp=0;
    for(int i=start;i<end;i++)
    {
        if(a[i]<=pivot)
        {
            temp=a[pindex];
            a[pindex]=a[i];
            a[i]=temp;
            pindex++;
        }
    }
    temp=a[end];
    a[end]=a[pindex];
    a[pindex]=temp;
    return pindex;
}

void quicksort(int a[],int start,int end)
{
    int pindex;
    if(start<end)
	{
	    pindex=partition(a,start,end);
	    quicksort(a,start,pindex-1);
	    quicksort(a,pindex+1,end);
	}
}
int main()
{
    printf("Enter size then elements");
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++)
	{
	    scanf("%d",&a[i]);
	}
    quicksort(a,0,n-1);
    for(int i=0;i<n;i++)
	{
	    printf("\n%d\n",a[i]);
	}
}
