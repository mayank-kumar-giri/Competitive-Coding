#include <stdio.h>
#include <stdbool.h>
#include <string.h>
struct edge {
    int x,y,w;
};

int getr(int value,int setr[]) //get representative of a set function
{
 	if(value==setr[value])
		return value;
	else setr[value]=getr(setr[value],setr);
}
int main()
{
    int n,e,i,j,mst_i,mstcost=0,count=0,seta,setb;
    mst_i=0;

    printf("enter numer of nodes\n");
    scanf("%d",&n);
    printf("enter number of edges\n");
    scanf("%d",&e);


    struct edge edges[e],mst[n-1],tmp;
	int setr[n];
    bool visited[n];
    memset(visited,false,sizeof(visited));
	for(i=0;i<n;i++)
	setr[i]=i;

    printf("enter vertices connected by edges and then wieght \n");
    for(i=0;i<e;i++){
        scanf("%d%d%d",&edges[i].x,&edges[i].y,&edges[i].w);
        --edges[i].x;--edges[i].y;
    }

    

    /*//
    simple sort can be replaced by custom merge sort which will reduce time complexity to O(eloge)
    now its O(e^2)
    */
    //algo start
    for(i=0;i<e-1;i++)
        for(j=i+1;j<e;j++)
            if(edges[i].w>edges[j].w)
                {tmp=edges[i];edges[i]=edges[j];edges[j]=tmp;}

    
    for(i=0;i<e;i++)
        {
			seta=getr(edges[i].x,setr);
			setb=getr(edges[i].y,setr);
            //printf("%d %d\n",seta,setb);
			if(seta==setb)
				continue;
			else{
				setr[seta]=setb;      //set representative of edges[i].x as edges[i].y
				mst[mst_i++]=edges[i];
			}
		}
    //algo finish


    printf("mst defined by\n");
    for(i=0;i<mst_i;i++){
        printf("%d %d \n",mst[i].x+1,mst[i].y+1);
		mstcost+=mst[i].w;
}
    printf("\nmst cost =%d\n",mstcost);

}
/*
 4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
 */