#include<iostream>
#include"merge.c"
#include"bs.cpp"
#include<cstdlib>
#define maxim 1000000
using namespace std;

int main()
{
    int n;
    cout<<"\nEnter no. of vertices ";
    cin>>n;
    char v[n];
    int ad[n][n],org[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            ad[i][j]=maxim;
        }
    }

    int min_i=0,min_j=0;
    cout<<"\nEnter the name of vertices(1 char only)\n";
    for(int i=0;i<n;i++) cin>>v[i];
    cout<<"\nEnter the name of vertices between which there is an edge along with its weight\n";
    char r='y',s,e;
    int w=0,is,ie,f=0,g=0;

    while(r!='n')
    {
        cin>>s>>e>>w;
        f=0;
        g=0;
        for(int i=0;i<n;i++)
        {
            if(f==1 && g==1) break;
            if(s==v[i])
            {
                is=i;
                f=1;
            }
            if(e==v[i])
            {
                ie=i;
                g=1;
            }
        }
        if(f==1 &&g==1)
        {
            if(ad[is][ie]>w)
            {
                ad[is][ie]=w;
                org[is][ie]=w;
            }
        }
        else cout<<"\nThere are no such vertices! :-(";
        cout<<"\nWanna continue(y/n)??";
        cin>>r;
    }
    const int z=(n*(n+1));
    int cis[z],mcost=0,temp,k=0;
    for(int i=0;i<z;i++) cis[i]=-1;
    for(int i=0;i<n;i++)
    {
        f=0;
        g=0;
        min_i=0;
        min_j=0;
        int mini=ad[0][0];
        ad[0][0]=maxim;
        for(int m=0;m<n;m++)
        {
            for(int j=1+m;j<n;j++)
            {
                if(ad[m][j]<mini)
                {
                    mini=ad[m][j];
                    min_i=m;
                    min_j=j;
                }
            }
        }
        int x=ad[min_i][min_j];
        ad[min_i][min_j]=maxim;
        temp=x;
        if(i>=1)
        {
            for(int l=0;l<k;l++)
            {
                if(f==1 & g==1) break;
                if(min_i==cis[l])
                {
                    f=1;
                }
                if(min_j==cis[l])
                {
                    g=1;
                }
            }
        }
        if(f==1&&g==1) continue;
        cis[k]=min_i;
        cis[k+1]=min_j;
        k=k+2;
        mcost=mcost+temp;
    }

    cout<<"\nThe Minimal Spanning Tree of the I/P graph by Kruskal's contains following edges: \n";
    for(int i=0;i<(2*n - 2);i+=2)
    {
        cout<<endl<<v[cis[i]]<<v[cis[i+1]]<<" with weight "<<org[cis[i]][cis[i+1]]<<"\n";
    }
    cout<<"\nAnd the cost of this MST is "<<mcost<<"!\n";
}
