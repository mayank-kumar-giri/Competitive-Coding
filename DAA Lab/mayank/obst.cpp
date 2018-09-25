#include<iostream>
using namespace std;
int main(){
    int n,i,j;
    cout<<"Enter number of nodes in BST : ";
    cin>>n;
    int l=n;
    float a[n],p[n+1],q[n+1];
    p[0]=0;
    cout<<"Enter the nodes: ";
    for(i=0;i<n;i++)
        cin>>a[i];
    cout<<"Enter the probability of searching an internal node: ";
    for(i=1;i<=n;i++)
        cin>>p[i];
    cout<<"Enter the probability of searching an external node: ";
    for(i=0;i<n+1;i++)
        cin>>q[i];
    int t=0,z=(n+2)*(n+1)/2,k=0;
    float w[n+1][n+1],c[n+1][n+1],r[n+1][n+1];
    for(i=0;i<z;i++){
        if(k==k+t)
            w[k][k+t]=q[k];
        else
            w[k][k+t]=p[k+t]+q[k+t]+w[k][k+t-1];
        if(k==l){
            k=0;
            t++;
            l--;
            continue;
        }
        k++;
    }
    t=0;k=0;l=n;
    for(i=0;i<z;i++){
        if(k==k+t){
            c[k][k+t]=0;
            r[k][k+t]=0;
        }
        else{
            int mini=10000000,index=-1;;
            for(j=k+1;j<=k+t;j++){
                if(mini>=(c[k][j-1]+c[j][k+t])){
                    mini=(c[k][j-1]+c[j][k+t]);
                    index=j;
                }
            }
            c[k][k+t]=mini+w[k][k+t];
            r[k][k+t]=index;
        }
        if(k==l){
            k=0;
            t++;
            l--;
            continue;
        }
        k++;
    }
    cout<<"\nThe search cost of a key in our OBST is "<<c[0][n]<<endl;
    return 0;
}
