#include<iostream>
#include"merge.c"
#include"bs.cpp"
using namespace std;
int main()
{
    int n;
    cout<<"\nEnter the no. of elements and then the elements: ";
    cin>>n;
    int a[n],b[n],fo[n];
    for(int i=0;i<n;i++) cin>>a[i];
    int cfi=0,f=0,j=0;
    for(int i=0;i<n;i++)
    {
        b[i]=a[i];
        fo[i]=0;
    }
    mergesort(a,n);
    for(int i=0;i<n-1;i++)
    {
        if(a[i]==a[i+1])
        {
            fo[j]=a[i];
            j++;
            i++;
        }
    }

    int i,k,cc;
    mergesort(fo,n);
    for(i=0;i<n;i++)
    {
        cc=bs(fo,b[i],0,n-1);
        if(cc!=-1)
        {
            f=1;
            cout<<"\nWe have found the first duplicate number in the array, its "<<b[i]<<", which is present at the indices "<<i<<" and ";
            break;
        }
    }
    if(f==1)
    {
        for(k=i+1;k<n;k++)
        {
            if(b[i]==b[k])
                {
                    cfi=k;
                    break;
                }
        }
        //cfi=bs(b,b[i],i+1,n-1);
        cout<<cfi<<"!!!\n";
    }
    if(f==0) cout<<"\nThere is no repeated element in this array!! :-( :-(";
}
