def itemBinarySearch(list, item):

    # Sort the list in ascending order 
    list.sort()

    # Get first and last position
    low = 0
    high = len(list)-1

    while (low <= high):
        mid = (low + high) // 2

        if (item == list[mid]):
            return mid+1
        elif (item > list[mid]):
            low = mid + 1
        elif (item < list[mid]):
            high = mid - 1

    return -1

