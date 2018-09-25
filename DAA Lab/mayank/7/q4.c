#include <stdio.h>
#include <stdbool.h>
#include "merge.c"
#include "bs.c"

int main()
{
    int n,i;
    printf("enter the number of elements in array\n");
    scanf("%d",&n);
    int a[n];
    bool flag=false;
    //mergesort(a,n);
    for ( i = 0; i < n; ++i)
        scanf("%d",&a[i]);
    mergesort(a,n);
    for ( i = 0; i < n-1; ++i){
        if (a[i]==a[i+1])
           flag=true;

    }
    if(flag)
        printf("duplicate elements exist\n");
    else
    printf("no duplicate elements present\n");

    return 0;
}
