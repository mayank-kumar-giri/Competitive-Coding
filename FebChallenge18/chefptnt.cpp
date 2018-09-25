#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,m,x,k,t=0;
        cin>>n>>m>>x>>k;
        char s[k];
        cin>>s;

        if(k>=n)
        {
            if(m<n && x<2)
            {
                cout<<"no\n";
            }
            else
            {
                int c=0,f=0,ce=0,co=0;
//                cout<<"hola\n";
                for(int l=0;l<k;l++)
                {
                    if(s[l]=='E') ce+=1;
                    else co+=1;
                }
//                cout<<"hola\n"<<ce<<" "<<co;
                for(int j=1;j<m+1;j++)
                {
                    if(f==1) break;
                    for(int k=0;k<x;k++)
                    {
                        if((j%2)==0)
                        {
                            if(ce>0)
                            {
                                ce=ce-1;
                                c=c+1;
                            }
                        }

                        else
                        {
                            if(co>0)
                            {
                                co=co-1;
                                c=c+1;
                            }
                        }

                        if(c>=n)
                        {
                            f=1;
                            break;
                        }

                        if(ce==0 && co==0)
                        {
                            f=1;
                            break;
                        }
                    }
                }
                if(c<n) cout<<"no\n";
                else cout<<"yes\n";

            }
        }
        else cout<<"no\n";
    }
}
