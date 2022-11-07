from leapYear import *

# Write a python program for check Leap Years.

def main():

    year = int(input("Enter a year: "))
    leapYear = checkLeapYear(year)

    if (leapYear == True):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")

if __name__ == "__main__":
    main()
