def BinarySearch(arr, s, e, k):

    # s>e matlab rukjao nhi mila or
    if(s>e):
        return False
    
    mid = (s + e)//2

    #mil gya bhai
    if (arr[mid] == k):
        return mid + 1

    if (arr[mid] < k ):
        return "ele is at this postion"+f" {BinarySearch(arr, mid+1, e, k)}"
    else:
        return "ele is at this postion"+f" {BinarySearch(arr, s, mid-1, k)}"




arr = [1,2,3,5,8]

print(BinarySearch(arr, 0, len(arr)-1, 5))