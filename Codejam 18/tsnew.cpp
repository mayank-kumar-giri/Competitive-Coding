#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int l=0;l<t;l++)
    {
        int n;
        cin>>n;
        int a[n],j=0,k=0,os,es;
        if(n%2 == 0)
        {
            os=n/2;
            es=n/2;
        }
        else
        {
            os=(n+1)/2;
            es=(n-1)/2;
        }
        int e[es],o[os];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            if((i+1)%2 == 0)
            {
                e[k]=a[i];
                k++;
            }
            else
            {
                o[j]=a[i];
                j++;
            }
        }
        sort(o,o+os);
        sort(e,e+es);

        /*cout<<endl;
        for(int i=0;i<os;i++) cout<<o[i]<<" ";
        cout<<endl;
        cout<<endl;
        for(int i=0;i<es;i++) cout<<e[i]<<" ";
        cout<<endl;*/

        int i=0,f=0;
        j=0;
        k=0;
        for(i=0;i<n;i++)
        {
            if((i+1)%2 == 0)
            {
                a[i]=e[k];
                k++;
            }
            else
            {
                a[i]=o[j];
                j++;
            }
        }



        /*cout<<endl;
        for(int i=0;i<n;i++) cout<<a[i]<<" ";
        cout<<endl;*/



        for(i=0;i<(n-1);i++)
        {

            if(a[i]>a[i+1])
            {
                f=1;
                break;
            }
        }
        if(f==1) cout<<"Case #"<<l+1<<": "<<i<<endl;
        else cout<<"Case #"<<l+1<<": OK"<<endl;
    }
}
