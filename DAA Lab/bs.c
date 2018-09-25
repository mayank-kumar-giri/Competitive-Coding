#include<iostream>
int bs(int arr[],int key,int low,int high)
    {
        if(low==high)
		{
		if(arr[low]==key) return low;
		else return -1;
		}
	int mid=(low+high)/2;
	if(arr[mid]==key) return mid;
	else if(arr[mid]>key) return bs(arr,key,low,mid-1);
	else return bs(arr,key,mid+1,high);
    }
int main()
{
    printf("Enter key,no. of elements and then the elements:")
}
