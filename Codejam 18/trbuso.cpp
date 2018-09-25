#include<iostream>
#include<cmath>
using namespace std;

int swaparr(int a[],int i,int j)
{
    int temp=a[i];
    a[i]=a[j];
    a[j]=temp;
}

int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++) cin>>a[i];
    bool done = false;
    while(!done)
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
    cout<<endl;
    for(int i=0;i<n;i++) cout<<a[i]<<" ";
    cout<<endl;
}
