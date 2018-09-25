#include<iostream>
#include "bs.cpp"
#include "merge.c"
using namespace std;

int main()
{
    int n,r;
    cout<<"Enter the sizes of array followed by elements: ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    int k;
    cout<<"Enter the value of K ";
    cin>>k;
    mergesort(arr,n);
    for(int i=0;i<n;i++)
    {
        r=bs(arr,k-arr[i],0,n-1);
        if(r!=-1)
        {
           cout<<"Yes!!!There are such 2 elements at position "<<i<<" and position "<<r<<endl;
           cout<<"Because "<<arr[i]<<" + "<<arr[r]<<" = "<<arr[i]+arr[r]<<" which is equal to k = "<<k<<endl;
           break;
        }
        if(i==n-1 && r==-1) cout<<"No!!!There are no such 2 elements whose sum is "<<k<<endl;
    }
}
