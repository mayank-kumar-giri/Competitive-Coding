//
// Created by hjoshi on 12/11/17.
//
#include<bits/stdc++.h>
using namespace std;
bool bsearch(int a[],int low,int high){
    int mid;
    while(low<=high){
        mid = (low+high)/2;
        if(a[mid]==mid+1)
            return true;
        else if((mid+1)>a[mid]){
            low = mid+1;
        }
        else
            high = mid-1;
    }
    return false;
}
int main(){
    int n,i,j;
    cout<<"Enter the no. of elements:";
    cin>>n;
    int a[n];
    cout<<"\nEnter the elements:";
    for(i=0;i<n;i++)
        cin>>a[i];
    if(bsearch(a,0,n-1))
        cout<<"yes"<<endl;
    else
        cout<<"no"<<endl;
}
