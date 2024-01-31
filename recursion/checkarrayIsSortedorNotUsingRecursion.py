def isSorted(arr, n): 
    
    # BASE CASE
    
    if (n==0 or n==1):
        return True
    
    if (arr[0]> arr[1]):
        return False
    
    else:
        return isSorted(arr[1:], n-1)


arr = [1,2,3]

arr2 = [2,4,8,9,9,1]

print(isSorted(arr=arr2, n=len(arr2)))