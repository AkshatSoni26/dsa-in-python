def Power(base, pow):
    
    isEven = pow%2 == 0
    
    #base case
    if(pow == 0):
        return 1
    
    #second base case:
    if(pow == 1):
        return base

    # pow is even
    if(isEven):
        return Power(base, pow/2) * Power(base, pow/2)

    # pow is odd
    else:
        return base * Power(base, (pow-1)/2) * Power(base, (pow-1)/2)




print(Power(3,9))