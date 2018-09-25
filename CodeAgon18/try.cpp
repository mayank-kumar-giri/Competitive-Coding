#include <bits/stdc++.h>
using namespace std;

#define INT_SIZE 32

// function to find the OR_SUM
int ORsum(int arr[], int n)
{
    // create an array of size 32
    // and store the sum of bits
    // with value 0 at every index.
    int zerocnt[INT_SIZE] = { 0 };

    for (int i = 0; i < INT_SIZE; i++)
        for (int j = 0; j < n; j++)
            if (!(arr[j] & 1 << i))
                zerocnt[i] += 1;

    // for each index the OR sum contributed
    // by that bit of subset will be 2^(bit index)
    // now the OR of the bits is 0 only if
    // all the ith bit of the elements in subset
    // is 0.
    int ans = 0;
    for (int i = 0; i < INT_SIZE; i++)
    {
        ans += ((pow(2, n) - 1) -
               (pow(2, zerocnt[i]) - 1)) *
                pow(2, i);
    }

    return ans;
}

// Driver code
int main()
{
    int arr[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << ORsum(arr, size);
    return 0;
}
