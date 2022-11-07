def isPalindrome(str):

    l = 0
    r = len(str)-1

    if (l >= r):
        return True
    
    if str[l] != str[r]:
        return False
    
    return isPalindrome(str[1:-1])


