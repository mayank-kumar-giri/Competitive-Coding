#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        long double d[n][3];
        long double l=0;
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<3;k++)
            {
                cin>>d[j][k];
            }
            long double temp = d[j][0];
            d[j][0] += (d[j][2]/100)*d[j][0];
            d[j][0] -= (d[j][2]/100)*d[j][0];
            l+=(d[j][1]*temp)-(d[j][1]*d[j][0]);
        }
        cout<<setprecision(18)<<l<<endl;
    }
}
