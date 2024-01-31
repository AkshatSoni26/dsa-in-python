def bubbleSort(arr, s , n):

    print(arr, 'n===>', n)

    #base case
    if(n==0 ):
        return arr
    
    for i in range(n):
        print('under the for===>',arr, 'n===>', n)
        if(arr[i]>arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i] 
    

    return bubbleSort(arr,s ,n-1)




arr = [5,4,3,2,1,10,2]

print(bubbleSort(arr, 0, len(arr)-1))