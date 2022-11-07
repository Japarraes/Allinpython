#from binarySearch import *

# Program to swap two numbers

def main():
    
    # Without Using third Variable
    a = 3
    b = 9
    print('before swapping')
    print('a =', a)
    print('b =', b)

    a = a + b  
    b = a - b 
    a = a - b  

    print('After swapping')
    print('a =', a)
    print('b =', b)

    # Pythonic way

    a = 2
    b = 8
    print('before swapping')
    print('a =',a)
    print('b =',b)

    a,b = b,a

    print('After swapping')
    print('a =',a)
    print('b =',b)

if __name__ == "__main__":
    main()
