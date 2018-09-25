#include<iostream>
#define mAX 1000000
using namespace std;

class cash
{
    public:
        int m;
        int s;
        int p;
};

void merges(cash arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    /* create temp arrays */
    cash L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i].s <= R[j].s)
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(cash arr[], int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l+(r-l)/2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merges(arr, l, m, r);
    }
}



int main()
{
    int t;
    cin>>t;
    for(int l=0;l<t;l++)
    {
        int r,b,c;
        cin>>r>>b>>c;
        cash a[c];
        for(int i=0;i<c;i++)
        {
            cin>>a[i].m>>a[i].s>>a[i].p;
        }
        mergeSort(a,0,c-1);
//        for(int i=0;i<c;i++)
//        {
//            cout<<a[i].m<<" "<<a[i].s<<" "<<a[i].p<<" ";
//        }
//        cout<<endl;
        int mmax=a[0].m;
        for(int i=1;i<c;i++)
        {
            if(a[i].m>mmax) mmax=a[i].m;
        }
        int poss[c][mmax];
        for(int i=0;i<c;i++)
            for(int j=0;j<mmax;j++)
                poss[i][j]=mAX;

        for(int i=0;i<c;i++)
        {
            int k=mmax;
            for(int j=0;j<mmax;j++)
            {
                if(a[i].m<k) break;
                poss[i][j]=(k*a[i].s)+a[i].p;
                k--;
            }
        }

        for(int i=0;i<c;i++)
        {
            for(int j=0;j<mmax;j++)
                cout<<poss[i][j]<<"     ";
            cout<<endl;
        }
    }

}
