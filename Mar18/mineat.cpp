#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
//unsigned long long iii=1;
unsigned long long f=0;

unsigned long long reqnn(unsigned long long p,unsigned long long a[],unsigned long long n)
{
    unsigned long long ans=0;
    for(unsigned long long i=p+1;i<n;i++)
    {
        long double x=a[i],y=a[p];
        ans+=ceil(x/y);
    }
    return ans;
}

unsigned long long reqnnL(unsigned long long p,unsigned long long a[],unsigned long long n,unsigned long long k)
{
    unsigned long long ans=0;
    for(unsigned long long i=p+1;i<n;i++)
    {
        long double x=a[i],y=k;
        ans+=ceil(x/y);
    }
    return ans;
}

unsigned long long mink(unsigned long long l,unsigned long long r,unsigned long long sum,unsigned long long n,unsigned long long a[],unsigned long long pp,unsigned long long h)
{
        if(l>r) return pp;
        unsigned long long p=(l+r)/2;
        unsigned long long nn=h-(p+1);
        unsigned long long z = reqnn(p,a,n);
//        cout<<iii<<"th iteration of mink() :\n";
//        cout<<"p="<<p<<" nn="<<nn<<" z="<<z<<" pp="<<pp<<endl;
//        iii++;
        if(nn==z) return p;
        else if (p==pp)
        {
            f=1;
            return p;
        }
        if(z>nn) return mink(p,r,sum,n,a,p,h);
        else return mink(l,p,sum,n,a,p,h);
}



int main()
{
    unsigned long long t;
    cin>>t;
    for(unsigned long long i=0;i<t;i++)
    {
        f=0;
        unsigned long long n,h;
        cin>>n>>h;
        unsigned long long a[n];
        for(unsigned long long j=0;j<n;j++)
        {
            cin>>a[j];
        }
        sort(a,a+n);
        unsigned long long sn2=0,sum=0,k;
        for(unsigned long long j=0;j<n;j++)
        {
            if(j<=(n-1)/2) sn2+=a[j];
            sum+=a[j];
        }

        k=mink(0,n-1,sum,n,a,0,h);
        if(f==1)
        {
            unsigned long long p=k;
            unsigned long long nn=h-(p+1);
            unsigned long long z=reqnn(p,a,n);
            unsigned long long ap,app;
            app=a[p];
            ap=a[p];
            while(z<=nn && ap>1)
            {
                app=ap;
                ap--;
                if(ap<a[p] && p>-1)
                {
                    nn++;
                    p--;
                }
                z=reqnnL(p,a,n,ap);
//                cout<<iii<<"th iteration of mink() :\n";
//                cout<<"ap="<<ap<<" nn="<<nn<<" z="<<z<<" app="<<app<<endl;
//                iii++;
            }
            while(z>nn)
            {
                app=ap;
                ap++;
                if(ap==a[p+1] && nn>0)
                {
                    nn--;
                    p++;
                }
                z=reqnnL(p,a,n,ap);
//                cout<<iii<<"th iteration of mink() :\n";
//                cout<<"ap="<<ap<<" nn="<<nn<<" z="<<z<<" app="<<app<<endl;
//                iii++;
            }
            cout<<ap<<endl;
        }
        else cout<<a[k]<<endl;
    }
}
