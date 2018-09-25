#include<iostream>
using namespace std;
int main()
{
    int n,i,j;
    cout<<"Enter number of matrices: ";
    cin>>n;
    int l=n;
    int p[n+2];
    cout<<"Enter the dimensions of the matrices: ";
    for(i=1;i<n+2;i++)
        cin>>p[i];
    int t=0,z=(n)*(n+1)/2,k=1;
    float m[n+1][n+1];
    for(i=0;i<z;i++)
    {
        if(k==k+t)
            m[k][k+t]=0;
        else
        {
            int mini=10000000;
            for(j=k;j<k+t;j++)
            {
                if(mini>=(m[k][j]+m[j+1][k+t]+p[k]*p[j+1]*p[k+t+1]))
                    mini=(m[k][j]+m[j+1][k+t]+p[k]*p[j+1]*p[k+t+1]);
            }
            m[k][k+t]=mini;
        }
        if(k==l)
        {
            k=1;
            t++;
            l--;
            continue;
        }
        k++;
    }
    cout<<m[1][n]<<endl;
    return 0;
}
