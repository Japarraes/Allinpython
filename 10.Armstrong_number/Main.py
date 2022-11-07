from armstrongNumber import *

# Check for Armstrong numbers
# Armstrong number is a number in which the sum of each digit powered to the total number of digits is same as the given number.
# Example:
#   - 153: 1^3 + 5^3 + 3^3 = 153
#   - 8208: 8^4 + 2^4 + 0^4 + 8^4 = 8208

def main():
    
    while True:
    
        try:
            number = int(input('ENter a number: '))
            break
        except Exception:
            print('only numbers are allowed pls enter again')
    
    if (isArmstrongNumber(number)):
        print(f"The number {number} is an Armstrong Number.")
    else:
        print(f"The number {number} is NOT an Armstrong Number.")

    
if __name__ == "__main__":
    main()
