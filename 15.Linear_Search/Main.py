from linearSearch import *

# what is linear search in python

def main():
    
    myList = [2, 4, 8, 23, 32, 1, 9]
    x = 0
    pos = itemLinearSearch(myList, x)

    if (pos == -1):
        print(f"Element {x} is not present")
    else:
        if (pos == 1):
            sufix = "st"
        elif (pos == 2):
            sufix = "nd"
        else:
            sufix = "th"
        
        print(f"Elemento {x} present at {pos}{sufix} position")
    
    print(myList)

if __name__ == "__main__":
    main()
