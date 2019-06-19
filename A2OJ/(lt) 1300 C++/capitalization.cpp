#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin>>s;

    for(int i=0;i<s.length();i++)
    {
        if(s[i]>='A' && s[i]<='Z' && i!=0)
        {
            s[i] = 'a' + (s[i]-'A');
        }
        else if(i==0 && s[i]>='a' && s[i]<='z')
        {
            s[i] = 'A' + (s[i]-'a');
        }
    }

    cout<<s;
}