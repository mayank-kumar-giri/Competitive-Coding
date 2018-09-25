#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int te;
    cin>>te;
    for(int j=0;j<te;j++)
    {
        string s;
        cin>>s;
        int p[s.size()];
        int a[30]={0};
        for(int i=0;i<s.size();i++)
        {
            int t=(s[i]-'a');
            a[t]++;
        }
        int oc=0,oi,f=0;

        for(int i=0;i<s.size();i++)
        {
            cout<<a[i]<<" ";
        }
        cout<<endl;

        for(int i=0;i<26;i++)
        {
            if(a[i]%2 != 0)
            {
                oi=i;
                oc++;
                f=1;
            }
        }
        if(f==0) oi=-1;
        cout<<endl<<endl<<oi<<endl<<endl;
        if(oc>1)
        {
            cout<<"-1"<<endl;
            continue;
        }
        int l=0,r=s.size()-1;
        cout<<endl<<oi<<endl;
        for(int i=0;i<s.size();i++)
        {
            if(i==oi)
            {
                int x=s.size()/2;
                p[x]==oi+1;
                continue;
            }
            int t=(s[i]-'a');
            if(a[t]%2 == 0)
            {
                p[l]=i+1;
                l++;
                a[t]--;
            }
            else
            {
                p[r]=i+1;
                r--;
                a[t]--;
            }
        }
        for(int i=0;i<s.size();i++)
        {
            cout<<p[i]<<" ";
        }
        cout<<endl;
    }
}
