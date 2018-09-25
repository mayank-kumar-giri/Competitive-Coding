#include<iostream>
using namespace std;

int swaparr(int a[],int i,int j)
{
    int temp=a[i];
    a[i]=a[j];
    a[j]=temp;
}

int main()
{
    int t;
    cin>>t;
    for(int l=0;l<t;l++)
    {
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++) cin>>a[i];
        bool done = false;
        while(done == false)
        {
            done = true;
            for(int i=0; i<n-2;i++)
            {
                if(a[i]>a[i+2])
                {
                    done = false;
                    swaparr(a,i,i+2);
                }
            }
        }
        int j=0,f=0;
        for(j=0;j<n;j++)
        {
            if(a[j]>a[j+1])
            {
                f=1;
                break;
            }
        }
        if(f==1) cout<<"Case #"<<l+1<<": "<<j<<endl;
        else cout<<"Case #"<<l+1<<": OK"<<endl;
    }
}
