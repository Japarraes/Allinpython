#from binarySearch import *

# Remove duplicates from the list

def main():
    
    # Option 1: Create a set from list. Set erase duplicate automatically
    arr = [7, 7, 7, 8, 8, 9, 9, 9, 1, 5]

    # set_arr = set(arr)
    # new_arr = list(set_arr)
    new_arr = list(set(arr))

    print(arr)
    print(new_arr)
    
    # Option 2: using loop
    # new_arr = []
    # for item in arr:
    #     if item not in new_arr:
    #         new_arr.append(item)

    # new_arr = []
    # for i in range(len(arr)):
    #     if i == arr.index(arr[i]):
    #         new_arr.append(arr[i])

    new_arr = [arr[i] for i in range(len(arr)) if i == arr.index(arr[i])]
    
    print(arr)
    print(new_arr)

if __name__ == "__main__":
    main()
