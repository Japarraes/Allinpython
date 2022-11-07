#from fibonacciNumbers import *
from fibonacciNumbersRecursive import *

# Write a python program for the Fibonacci series by recursive method

def main():

    end = False
    while (end == False):
        num = int(input("Enter number for series: "))
        if (num <= 0):
            print("Enter a valid number (>0)")
        else:
            end = True

    fibo_numbers = [str(getFibonacciNumbers(i)) for i in range(0, num)]
    
    print(", ".join(fibo_numbers))

if __name__ == "__main__":
    main()
