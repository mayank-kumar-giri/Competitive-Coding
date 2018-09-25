#include <stdio.h>
int main()
{
    int i,j,n,m,tmp;

    printf("capcacity:\t");
    scanf("%d",&m);
    printf("number of objects\t");
    scanf("%d",&n);

    int w[n],p[n],pa[n];
    float x[n],maxprofit;
    maxprofit=0;
    for(i=0;i<n;i++)
    {
        pa[i]=i;
        x[i]=0.0;
    }

    printf("profit and wieghts respectively\n");

    for(i=0;i<n;i++) scanf("%d%d",&p[i],&w[i]);




    for(i=0;i<n-1;i++){
        for(j=i+1;j<n;j++)
            if(p[pa[i]]/(w[pa[i]]+0.0)<p[pa[j]]/(w[pa[j]]+0.0))
                {
                    tmp=pa[i];
                    pa[i]=pa[j];
                    pa[j]=tmp;
                }

    }
    for(i=0;i<n;i++)
    {
        if(m>=w[pa[i]])
        {
            m-=w[pa[i]];
            x[pa[i]]=1.0;
        }
        else break;
    }
    if(i<n)
        x[pa[i]]=m/(w[pa[i]]+0.0);

    for(i=0;i<n;i++)
    {
        printf("x[%d]=%.1f\n",i,x[i]);
        maxprofit+=x[i]*p[i];
    }
    printf("max profit=%f\n",maxprofit);
}
