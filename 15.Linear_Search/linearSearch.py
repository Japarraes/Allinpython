def itemLinearSearch(list, item):

    i = 0
    while (i < len(list)):
        if (list[i] == item):
            return i+1
        i += 1
        
    return -1
