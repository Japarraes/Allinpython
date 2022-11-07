def isArmstrongNumber(num):

    sum = 0
    str_num = str(num)
    power = len(str_num)

    for i in range(power):
        sum += int(str_num[i])**(power)
    
    if (sum == num):
        return True
    else:
        return False