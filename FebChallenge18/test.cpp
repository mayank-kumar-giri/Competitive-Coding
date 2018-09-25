#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    vector<int> arr;
    arr.assign(2,24);
    cout<<arr[1]<<endl<<sizeof(arr)/sizeof(arr[0])<<endl;
    int a=count(arr.begin(),arr.end(),24);
    string s="mayank";
    int pos=s.find('n');
    s.erase(pos,1);
    cout<<a;
    if('0'<='a' && '0'<='z') cout<<"\nYahoo\n"<<s;
    cout<<endl<<a;
}
