#include  <iostream>
using namespace std;
int shellSort(int arr[], int n)
{

    for (int gap = n/2; gap > 0; gap /= 2)
    {

        for (int i = gap; i < n; i++)
        {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
            arr[j] = temp;
        }
    }
    return 0;
}

int main()
{
    int arr[5] = {120, 134, 954, 12, 53},i;

    cout << "Array before sorting: \n";
    for (int i=0; i<5; i++)
        cout << arr[i] << " ";

    shellSort(arr, 5);

    cout << "\nArray after sorting: \n";
    for (int i=0; i<5; i++)
        cout << arr[i] << " ";

    return 0;
}
