#include <stdio.h>
#include <stdbool.h>
#include "merge.c"
#include "bs.c"
#define left (2*(i+1)-1)
#define right (2*(i+1))

bool findpair(int *a,int low,int high,int sum)
{
while(low<high)
{

if(sum==a[low]+a[high])
{
printf("required elements are\t:%d %d",a[low],a[high]);
return true;
}
else if(sum>a[low]+a[high])
low++;
else if(sum<a[low]+a[high])
high--;
}
return false;
}




int main()
{
int n,k,i;
printf("enter number of elements and sum required");
scanf("%d %d",&n,&k);
int a[n];
printf("enter elements\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
mergesort(a,n);
for( i=0;i<n-2;i++){

if(findpair(a,i+1,n-1,k-a[i]))
printf(" %d\n",a[i]);

}


}
