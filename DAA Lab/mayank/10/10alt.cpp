#include<iostream>
#include"merge.c"
#include"bs.cpp"
using namespace std;
int main()
{
    int n,f=0;
    cout<<"\nEnter the no. of elements and then the elements: ";
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++) cin>>a[i];
    int i=0,j=0;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[j]==a[i])
            {
                f=1;
                break;
            }
        }
        if(f==1) break;
    }
    if(f==0) cout<<"No repeat";
    else cout<<"REPEAT "<<a[i]<<" at indices "<<i<<" and "<<j<<"!!!";
}
