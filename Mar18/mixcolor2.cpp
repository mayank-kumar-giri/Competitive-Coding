#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,ans=0;
        cin>>n;
        int c[n];
        for(int j=0;j<n;j++)
        {
            cin>>c[j];
        }
        sort(c,c+n);
        int temp=c[0];
        for(int j=1;j<n;j++)
        {
            if(c[j]==temp) ans++;
            else
            {
                temp=c[j];
                continue;
            }
        }
        cout<<ans<<endl;
    }
}
