def sumOfArray(arr, n):
    
    if (n==0):
        return 0
    return arr[n-1] + sumOfArray(arr[:n-1], n-1)



a = [1,2,10,10]

print(sumOfArray(arr=a, n=len(a)))