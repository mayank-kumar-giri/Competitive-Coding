#include<iostream>
#include"merge.c"
#include"bs.cpp"
#include<cstdlib>
using namespace std;
int main()
{
    for(int i=1;i<8800;i++)
    {
        cout<<i<<endl;
    }
    for(int i=0;i<197;i++) cout<<(rand()%2000 + 1556)<<endl;
}
