#include<iostream>
#include<string>
using namespace std;
int main()
{
    unsigned long long t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        string s;
        cin>>s;
        unsigned long long n=s.length(),f=0,ss=0;
//        cout<<endl<<endl<<n<<endl;
        unsigned long long p[n];
        for(int z=0;z<n;z++)
        {
            p[z]=0;
        }
        unsigned long long l=0,m=n-1;

        for(int j=0;j<n;j++)
        {
            if((p[l]!=0)&&(p[m]!=0)) break;
            if(s[j]>='a' && s[j]<='z')
            {
                p[l]=j+1;
                l++;
                char t=s[j];
                s[j]='0';
                unsigned long long pos;
//                int pos=s.find(t);
                for(int z=0;z<n;z++)
                {
                    if(s[z]==t)
                    {
                        pos=z;
                        break;
                    }
                }
                if(s[pos]==t)
                {
                    s[pos]='0';
                    p[m]=pos+1;
                    m--;
                }
                else if((s[pos]!=t)&&(ss==0))
                {
                    l--;
                    p[l]=0;
                    unsigned long long tem = n/2;
                    p[tem]=j+1;
                    s[j]='0';
                    ss=1;
                }
                else
                {
                    cout<<"-1\n";
                    f=1;
                }

            }
            if(f==1) break;
        }
        if(f==0)
        {
            for(int j=0;j<n;j++)
            {
                if(j!=(n-1)) cout<<p[j]<<" ";
                else cout<<p[j]<<"\n";
            }
        }

    }
}
