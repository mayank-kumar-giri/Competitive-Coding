#include <stdio.h>
int main()
{
    int i,j,n,tmp;
    printf("number of jobs:\t");
    scanf("%d",&n);
    printf("enter job's profit and deadline respct.\n");

    int dead[n],profit[n],pa[n],slot[n],Maxprofit;
    Maxprofit=0;
    for( i=0;i<n;i++)
    {
        scanf("%d%d",&profit[i],&dead[i]);
        slot[i]=-1;
        pa[i]=i;
    }

    for( i=0;i<n-1;i++)
        for(j=i+1;j<n;j++)
            if(profit[pa[i]]<profit[pa[j]])
            {
                tmp=pa[j];
                pa[j]=pa[i];
                pa[i]=tmp;
            }

    for(i=0;i<n;i++)

    {
        for(j=dead[pa[i]]-1;j>=0;j--)
            if(slot[j]==-1)
            {
                slot[j]=pa[i];
                Maxprofit+=profit[pa[i]];
                break;
            }
    }


    printf("Sequence:\n");
    for(i=0;i<n;i++)
    if(slot[i]!=-1)
        printf("j%d ",slot[i]+1);
    printf("\n Maxprofit=%d\n",Maxprofit);

}
