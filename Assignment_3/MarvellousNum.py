def ChkPrime(value):
    count = 0
    for i in range(1,value+1):
        if(value % i) == 0:
            count = count+1
    if count > 2:
        return False
    else :
        return True