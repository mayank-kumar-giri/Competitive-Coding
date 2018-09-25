#include <stdio.h>
#include <stdbool.h>
#include <string.h>
int main()
{
    int i,n,j,tmp;
    scanf("%d",&n);
    int a[n];
    for( i=0;i<n;i++) scanf("%d",&a[i]);
    for( i=0;i<n-1;i++)
        for(j=i+1;j<n;j++)
            if(a[i]>a[j])
            {
                tmp=a[j];
                a[j]=a[i];
                a[i]=tmp;
            }
    for( i=0;i<n;i++) printf("%d ",a[i]);
}
