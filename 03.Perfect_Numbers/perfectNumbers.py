from array import array


def checkPerfectNumber(n):

    sum = 0
    numbers = ([])
    
    for i in range(1, n):
        if n % i == 0:
            numbers.append(i)
            sum += i
    
    if sum == n:
        return numbers, True
    else:
        return numbers, False
