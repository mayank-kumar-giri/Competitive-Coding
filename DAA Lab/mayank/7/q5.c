#include <stdio.h>
#include <stdbool.h>
#include "merge.c"
#include "bs.c"

int main()
{
    int n,i,maxind=0,cur,c=0,mxc;
    printf("Enter the number of elements\n");
    scanf("%d",&n);
    int a[n];
    for ( i = 0; i < n; ++i)
    scanf("%d",&a[i]);
    mergesort(a,n);
    maxind=0;
    cur=a[0];
    c=1;
    mxc=1;

    for ( i = 1; i < n; ++i)
        {

            if(a[i]!=cur){
                cur=a[i];c=1;
            }
            else
                c++;
            if(c>mxc){
                maxind=i;mxc=c;
            }
        }
    printf("max frequency is of %d present %d times\n",a[maxind],mxc);
    return 0;
}
