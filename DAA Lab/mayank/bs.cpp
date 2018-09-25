#include<iostream>
using namespace std;
int bs(int arr[],int key,int low,int high)
    {
        if(low<=high)
		{
            int mid=(low+high)/2;
            if(arr[mid]==key) return mid;
            else if(arr[mid]>key)
            {
                return bs(arr,key,low,mid-1);
            }
            else
            {
                return bs(arr,key,mid+1,high);
            }
		}
		else return -1;
    }
