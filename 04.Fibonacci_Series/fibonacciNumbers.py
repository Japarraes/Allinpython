def getFibonacciNumbers(n):

    a = 0
    b = 1
    fib_numbers = ([])

    if (n == 1):
        fib_numbers.append(a)
    elif (n == 2):
        fib_numbers.append(a)
        fib_numbers.append(b)
    else:
        i = 0
        while (i < n-2):
            c = a + b
            fib_numbers.append(c)
            a = b
            b = c
            i += 1

    return fib_numbers
