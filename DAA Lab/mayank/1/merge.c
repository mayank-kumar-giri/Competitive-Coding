#include<stdio.h>
void merge(int l[],int r[],int a[],int nl,int nr,int n)
{
    int i=0,j=0,k=0;
    while(i<nl && j<nr)
    {
        if(l[i]<r[j])
        {
           a[k]=l[i];
           i++;
        }
        else
           {
              a[k]=r[j];
              j++;
           }
            k++;
    }
    while(i<nl)
    {
        a[k]=l[i];
        i++;
        k++;
    }
    while(j<nr)
    {
        a[k]=r[j];
        j++;
        k++;
    }
}


void mergesort(int a[],int n)
{
    int i=0;
    if(n<2) return;
    int mid=n/2;
    int nl=mid,nr=n-mid,l[nl],r[nr];
    for(i=0;i<mid;i++)
	{
	    l[i]=a[i];
	}
    for(i=mid;i<n;i++)
	{
	    r[i-mid]=a[i];
	}
    mergesort(l,nl);
    mergesort(r,nr);
    merge(l,r,a,nl,nr,n);
}

