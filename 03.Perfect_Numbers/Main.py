from perfectNumbers import *

# Check is a number is a "perfect number": A number which is equal to sum of it’s divisors is known as perfect number.
# Example: 6 —-> divisor of 6 is 1,2,3 and sum of 1+2+3 = 6, that means 6 is perfect number.

def main():
    num = 6
    info_number = checkPerfectNumber(num)
    
    if (info_number[1]):
        print(f"The number {num} is a perfect number")
    else:
        print(f"The number {num} is a not perfect number")

    print(f"Divisors of '{num}' are: ", end="")
    divisors = info_number[0]
    for item in divisors:
        print(item, end=", ")

if __name__ == "__main__":
    main()
