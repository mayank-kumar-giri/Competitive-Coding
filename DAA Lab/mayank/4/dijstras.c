#include <stdio.h>
#include <stdbool.h>
#include <string.h>


void printfor(int i,int source ,int comesfrom[])
{
    if(i==source)
    {
        printf("%d ",i+1 );
    }
    else 
    {
        printfor(comesfrom[i],source,comesfrom);
        printf("->%d",i+1);
    }
}

int main()
{
    
    int n,e,i,j,mstcost=0,x,y,w,u,mpath_i=0,inf=99999,source;
    
    printf("enter numer of nodes\n");
    scanf("%d",&n);
    printf("enter number of edges\n");
    scanf("%d",&e);
	printf("enter source \n");
	scanf("%d",&source);
	source--;
    

    int mincost[n],comesfrom[n],adj[n][n];
    bool flag,in_mpath[n];//int mpath[n];

    
	memset(comesfrom,-1,n*sizeof(int));    
    memset(in_mpath,false,n*sizeof(bool));

	for(i=0;i<n;i++)
	{
	mincost[i]=inf;
		for(j=0;j<n;j++)
	adj[i][j]=inf;
	}

    printf("enter vertices connected by edges and then wieght \n");



    for(i=0;i<e;i++)
    {
        scanf("%d%d%d",&x,&y,&w);
        if(adj[--x][--y]>w)//case of multiple edge
            adj[x][y]=adj[y][x]=w;        
    }

    //algo start
    mincost[source]=0;
    for(mpath_i=0;mpath_i<n;mpath_i++)
    {
        flag=false;

        for(i=0;i<n;i++)
            if((!flag||mincost[i]<mincost[u])&&!in_mpath[i])            
                u=i,flag=true;           
        
        in_mpath[u]=true;
        
        for(i=0;i<n;i++)
            if(adj[u][i]!=inf&&mincost[i]>mincost[u]+adj[u][i]){
                mincost[i]=mincost[u]+adj[u][i];
                comesfrom[i]=u;
            }
            
    }
    //algo finish
    /*printf("shortsest defined by edges\n");
    for ( i = 1; i < n; ++i)
    {
        mstcost+=mincost[i];
        printf("%d  %d\n",i,comesfrom[i]);
    }*/
    for(i=0;i<n;i++)
	if(i!=source){
	    printf(" \nmincost[%d]=%d\n",i+1,mincost[i]);
        printfor(i,source,comesfrom);
    }

    return 0;
}
/*
 * 1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1
 */