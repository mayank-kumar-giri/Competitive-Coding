#include <bits/stdc++.h>

using namespace std;

int main()
{
    string l1,ol;
    cin>>l1;
    int m = (int)(l1[0] - '0'),n = (int)(l1[2] - '0'),k = (int)(l1[4] - '0');
    int x[k],y[k];
    int arr[m][n];
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            arr[i][j] = 0;
        }
    }
    for(int i=0;i<k;i++)
    {
        cin>>ol;
        x[i] = (int)(ol[0] - '0');
        y[i] = (int)(ol[2] - '0');
        arr[x[i]][y[i]] = -5;
    }
    int c=0;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            //if(arr[i][j]==-5) continue;
            int manh[k];
            for(int p=0;p<k;p++)
            {
                manh[p] = abs(i-x[p])+abs(j-y[p]);
            }
            sort(manh,manh+k);
            if(manh[0]==manh[1]) c++;
        }
    }
    cout<<c;
}
