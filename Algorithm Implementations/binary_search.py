def bin_search(arr,l,r,key):
    if l<=r:
        mid = int((l+r)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return bin_search(arr,l,mid-1,key)
        else:
            return bin_search(arr, mid+1, r, key)
    else:
        return -1