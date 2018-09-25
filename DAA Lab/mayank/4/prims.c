#include <stdio.h>
#include <stdbool.h>
#include <string.h>
int main()
{

    int n,e,i,j,mstcost=0,x,y,w,u,mstset_i=0,inf=99999;

    printf("enter numer of vertices\n");
    scanf("%d",&n);
    printf("enter number of edges\n");
    scanf("%d",&e);


    int mincost[n],parent[n],ad[n][n];
    bool flag,in_mstset[n];//int mstset[n];


    memset(parent,-1,n*sizeof(int));
    memset(in_mstset,false,n*sizeof(bool));

	for(i=0;i<n;i++)
	{
	mincost[i]=inf;
		for(j=0;j<n;j++)
	ad[i][j]=inf;
	}

    printf("enter vertices connected by edges and then wieght \n");



    for(i=0;i<e;i++)
    {
        scanf("%d%d%d",&x,&y,&w);
        if(ad[--x][--y]>w)//cade of multiple edge
            ad[x][y]=ad[y][x]=w;
    }

    //algo start
    mincost[0]=0;
    for(mstset_i=0;mstset_i<n;mstset_i++)
    {

        flag=false;

        for(i=0;i<n;i++)
            if((!flag||mincost[i]<mincost[u])&&!in_mstset[i])
                u=i,flag=true;
        //printf("@%d",u);
        in_mstset[u]=true;

        for(i=0;i<n;i++)
            if(ad[u][i]!=inf&&mincost[i]>ad[u][i]&&parent[u]!=i){
                mincost[i]=ad[u][i];
                parent[i]=u;
            }

    }
    //algo finish
    printf("Our MST is defined by following edges\n");
    for ( i = 1; i < n; ++i)
    {
        mstcost+=mincost[i];
        printf("%d  %d\n",i+1,parent[i]+1);
    }
    printf("MST cost=%d\n",mstcost );

    return 0;
}
