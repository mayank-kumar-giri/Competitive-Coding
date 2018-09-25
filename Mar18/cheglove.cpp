#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        int f[n],g[n];
        for(int j=0;j<n;j++)
        {
            cin>>f[j];
        }
        int f1=0,f2=0;
        for(int j=0;j<n;j++)
        {
            cin>>g[j];
            if(f[j]>g[j]) f1=1;
        }
        for(int j=0,k=n-1;j<n,k>=0;j++,k--)
        {
            if(f[k]>g[j]) f2=1;
        }
        if(f1==1 && f2==1) cout<<"none\n";
        else if(f1==0 && f2==1) cout<<"front\n";
        else if(f1==1 && f2==0) cout<<"back\n";
        else cout<<"both\n";

    }
}
