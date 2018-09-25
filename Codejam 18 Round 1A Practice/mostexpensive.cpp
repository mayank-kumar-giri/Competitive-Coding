#include<iostream>
using namespace std;
bool aisbigger(string a,string b)
{
    if(a.length()>b.length()) return true;
    else return false;
}

int main()
{
    int n,m;
    cin>>n>>m;
    int c[26];
    for(int i=0;i<26;i++) cin>>c[i];
    string a,b,temp,oth;
    cin>>a>>b;

    if(aisbigger(a,b))
    {
        temp=b;
        oth=a;
    }
    else
    {
        temp=a;
        oth=b;
    }

    string sub,csub;
    int ccost=0,cost=0,q=0;

    for(int i=0;i<temp.length();i++)
    {
//        cout<<"\nSub - "<<sub<<"\nCost - "<<cost<<"\nCsub - "<<csub<<"\nCcost - "<<ccost<<endl;
        if(csub.empty())
        {
            q=-1;
            q=oth.find(temp[i]);
//            cout<<endl<<q<<endl;
            if(q==-1) continue;
            else
            {
                csub=temp[i];
                ccost=c[temp[i]-'a'];
            }
            continue;
        }

        if(oth[q+1]==temp[i])
        {
            char* t=&temp[i];
            csub.append(t,csub.length()-1,1);
//            cout<<"\nYEAH "<<csub<<endl;
            ccost+=c[temp[i]-'a'];
            q++;
        }
        else
        {
            if(sub.empty())
            {
                sub=csub;
                cost=ccost;
            }
            else
            {
                if(ccost>cost)
                {
                    cost=ccost;
                    sub=csub;
                }
            }
            q=oth.find(temp[i]);
            if(q==-1) continue;
            else
            {
                csub=temp[i];
                ccost=c[temp[i]-'a'];
            }
        }
    }
    cout<<cost;
//    cout<<"\nHere's our most expensive subsequence with that cost: \n"<<"String -    "<<sub<<endl<<cost<<endl;
}
