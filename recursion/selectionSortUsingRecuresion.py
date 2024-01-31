def selectionSort(arr, s, n):
    
    print('selestion sort===>', arr)
    #base case
    if(s==n):
        return arr

    for i in range(s+1,n):
        print('under the for loop===>', arr)
        if(arr[s]>arr[i]):
            arr[s], arr[i] = arr[i], arr[s]
            print('under the for loop if condition===>', arr)

    return selectionSort(arr,s+1 ,n)



arr = [6,5,4,3,2,1]

print(selectionSort(arr, 0, len(arr)))