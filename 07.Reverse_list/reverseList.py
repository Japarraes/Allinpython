def getReverseList(list):

    # Get first and last position
    first = 0
    last = len(list) - 1

    recursive_list(list, first, last)
    
    return list


def recursive_list(my_list, f, l):
    
    if (f >= l):
        return my_list

    temp = my_list[f]
    my_list[f] = my_list[l]
    my_list[l] = temp

    return recursive_list(my_list, (f + 1), (l - 1))


