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
        int c[n],p=0,t[n];
        for(int j=0;j<n;j++)
        {
            cin>>c[j];
        }
        int z=0,f=0,cou=0,ans=0;
        for(int j=0;j<n;j++)
        {
            f=0;
            cou=0;
            for(int l=0;l<z;l++)
            {
                if(t[l]==c[j])
                {
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                t[z]=c[j];
                z++;
            }
            else
            {
                continue;
            }
            for(int k=j+1;k<n;k++)
            {
                if(c[k]==c[j]) cou++;
            }
            ans+=cou;
        }
        cout<<ans<<endl;
    }
}
