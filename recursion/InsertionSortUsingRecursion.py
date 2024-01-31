def InsertionSort(arr, i, n):

    #base case
    if(i==n):
        return arr
    
    key=arr[i]  # 5

    j = i-1 # 13
    
    while ((j>=0) and (arr[j] > key)):
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = key 
    

    return InsertionSort(arr,i+1 , n)

arr = [12, 11, 13, 5, 6]

print(InsertionSort(arr=arr,i=1 ,n=len(arr)))