#include <stdio.h>
#include <stdbool.h>

#include "merge.c"
#include "bs.c"

bool bse(int a[],int low,int high,int key)
{
int mid=(low+high)/2;
if(a[high]<key||a[low]>key)
return false;
if(high-low<2)
return (a[low]==key||a[high]==key);

return a[mid]==key||(a[mid]<key&&bs(a,mid+1,high,key)||(a[mid]>key&&bs(a,low,mid-1,key)));

}

int main()
{
    int n,m,i,k;
    bool flag=false;
    printf("enter number of elements for both a and b and sum required\n");
    scanf("%d%d%d",&n,&m,&k);
    int a[n],b[m];
    for ( i = 0; i < n; ++i)
        scanf("%d",&a[i]);

    for ( i = 0; i < m; ++i)
        scanf("%d",&b[i]);
    mergesort(b,m);
    for ( i = 0; i < n; ++i)
        if(bse(b,0,m-1,k-a[i]))
            flag=true;

    if (flag)
        printf("yes\n");
    else
        printf("no\n");

    return 0;
}
