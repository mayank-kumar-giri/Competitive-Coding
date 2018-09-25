#include <stdio.h>


//insertion sort


int main() {
    int n,i,j,tmp;
    printf("enter number of elemments\n");
    scanf("%d",&n);
    int a[n];
    printf("enter elements\n");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for( i=1;i<n;i++)
    {
        tmp=a[i];
        j=i-1;
        while(j>=0&&a[j]>tmp)
        {
            a[j+1]=a[j];
            j--;
        }
        j++;
        a[j]=tmp;
    }
    for(i=0;i<n;i++)
        printf("%d ",a[i]);
}
