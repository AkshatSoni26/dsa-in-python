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
            print('element is posioned',arr)
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    print(f'element is poistioned ar is correct position at index {j} from {s}',arr)

    return j
            



def QuickSort(arr, s, e):
    if(s<e):
        pi = partiona(arr, s, e)

        print("arr after partioning ======> ", pi)

        #quick sort in the left part
        QuickSort(arr, s, pi-1)
        print("============left portion============")

        #quick sort in the right part
        QuickSort(arr, pi+1, e) 
        print("============right portion============")


        return arr
    
    return arr


arr = [4,6,2,5,7,9,1,3]

print(QuickSort(arr, 0, len(arr)-1))