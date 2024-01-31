def partiona(arr, s, e):
    pivot = arr[s]
    i = s
    j = e

    while (i<j):
        #is left portion is small then goto next one
        while ((arr[i]<=pivot) and (i<=e)):
            i += 1
        
        #is right part is less than over pivot 
        while (( arr[j] > pivot ) and (j >= s)):
            j -= 1
        
        if ( i < j ):
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]

    return j
            



def QuickSort(arr, s, e):
    if(s<e):
        pi = partiona(arr, s, e)

        print("arr after partioning ======> ", pi)

        #quick sort in the left part
        QuickSort(arr, s, pi-1)

        #quick sort in the right part
        QuickSort(arr, pi+1, e) 

        return arr
    
    else:
        return arr


arr = [4,6,2,5,7,9,1,3]

print(QuickSort(arr, 0, len(arr)-1))