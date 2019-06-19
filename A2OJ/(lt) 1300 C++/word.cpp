//
// Created by Mayank Kumar Giri on 18-06-2019.
//

#include <iostream>

using namespace std;

int main()
{
    string str;
    cin>>str;

    int lc = 0, uc = 0;

    for(int i=0;i<str.length();i++)
    {
        if(str[i]<='z' && str[i]>='a') lc++;
        else uc++;
    }
    if(lc>=uc)
    {
        for(int i = 0; i < str.length() ; ++i)
        {
            if(str[i]<='Z' && str[i]>='A')
            {
                str[i] = 'a' + (str[i]-'A');
            }
        }
    }
    else
    {
        for(int i = 0; i < str.length() ; ++i)
        {
            if(str[i]<='z' && str[i]>='a')
            {
                str[i] = 'A' + (str[i]-'a');
            }
        }
    }

    cout<<str;

    return 0;
}