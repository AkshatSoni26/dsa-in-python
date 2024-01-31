def FindEle(arr, target):
    
    #base case
    if(len(arr) == 0):
        return False
    
    #base case
    if(arr[0]== target):
        return True
    
    
    return FindEle(arr[1:],  target=target)



a = [3,5,1,2,6]

print(FindEle(arr=a, target=1))