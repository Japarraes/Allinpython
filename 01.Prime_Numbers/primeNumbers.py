def primeNumbers_withFor(n):

    primeNums = ([])
    
    for i in range (2, n+1):
        for j in range (2, n+1):
            
            # Check if mod is zero
            if (i % j == 0):
                break 

        if (i == j):
            primeNums.append(i)

    return primeNums

def primeNumbers_withWhile(n):

    primeNums = ([])
    
    i = 2
    while (i <= n):
        j = 2
        
        while (j < n):
            # Check if mod is zero
            if (i % j == 0):
                break 
            j += 1

        if (i == j):
            primeNums.append(i)
        i += 1
        
    return primeNums