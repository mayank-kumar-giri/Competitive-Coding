#include<iostream>
#include<cmath>
using namespace std;

int damagecalc(string s)
{
    int n=s.length();
    int val=1,dam=0;
    for(int i=0;i<n;i++)
    {
        if(s[i]=='C') val*=2;
        else dam+=val;
    }
    return dam;
}

int main()
{
    int t;
    cin>>t;
    for(int l=0;l<t;l++)
    {
        int d;
        string p;
        cin>>d>>p;
        int n=p.length(),h=0,cdam=0,f=0;
        cdam=damagecalc(p);
        if(cdam<=d) cout<<"Case #"<<l+1<<": 0\n";
        else
        {
            for(int i=n-1;i>=0;i--)
            {
                if(p[i]=='S' && p[i-1]=='C')
                {
                    char temp;
                    temp=p[i];
                    p[i]=p[i-1];
                    p[i-1]=temp;
                    h++;
                    cdam=damagecalc(p);
                    if(cdam<=d) f=1;
                    else
                    {
                        i=n;
                    }
                }
                if(f==1) break;
            }
            if(f==1) cout<<"Case #"<<l+1<<": "<<h<<endl;
            else cout<<"Case #"<<l+1<<": IMPOSSIBLE\n";
        }
    }
}
