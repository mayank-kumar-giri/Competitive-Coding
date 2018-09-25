#include<iostream>
#include<cmath>
using namespace std;

bool checkifpalindrome(unsigned long long n)
{
    unsigned long long d=0,temp=n;
    while(temp!=0)
    {
        temp/=10;
        d++;
    }
    int num[d];
    temp=n;
    for(int i=d-1;i>=0;i--)
    {
        num[i]=temp%10;
        temp/=10;
    }
    for(int i=0,j=d-1;i<d/2;i++,j--)
    {
        if(num[i]!= num[j]) return false;
    }
    return true;
}

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        unsigned long long l,h,tl,th;
        cin>>l>>h;
        unsigned long long sl,sh;
        unsigned long long sli,shi,coun=0;
        tl=l;
        th=h;
        sli=ceil(sqrt(tl));
        tl=sli*sli;
//        cout<<"\nHi I am -sli- , "<<sli<<endl;
        bool x,y;
        while(tl<=th)
        {
            x=checkifpalindrome(tl);
            y=checkifpalindrome(sli);
            if(x && y)
            {
                coun++;
//                cout<<tl<<" ";
            }

            sli++;
            tl=sli*sli;
        }
//        cout<<endl;
        cout<<"Case #"<<i+1<<": "<<coun<<endl;
    }
}
