//
// Created by Mayank Kumar Giri on 17-06-2019.
//
#include <iostream>
using namespace std;

int main()
{
    string s;
    cin>>s;

    int lc = 0, uc = 0;

    for(int i=0;i<s.length();i++)
    {
        if(s[i]<="z" && s[i]>="a") lc++;
        else uc++;
    }
    if(lc>=uc)
    {
        for(int i = 0; i < s.length() ; ++i)
        {
            if(s[i]<="z" && s[i]>="a")

        }
    }

    return 0;
}
