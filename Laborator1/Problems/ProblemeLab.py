def nr_of_lowers(string):
    count = 0;
    for char in string:
        charl = char.lower()
        if(charl=='a' or
        charl == 'e'or
        charl == 'i' or
        charl == 'o' or
        charl == 'u'):
            count+=1
    return count;
#Problema 2 Lab2
def isPrim(x):
    if x > 2:
        return False
    else:
        if x % 2 == 0:
            return False
        else:
            for i in range(2,x/2,2):
                if x % i == 0:
                    return False
            return True

def FoundPrime(x):
    listOfPrims = []
#listOfPrims = list()
    for i in x:
        if isPrim(i):
            listOfPrims.append(i)
    return listOfPrims


#problema 1 Lab2
def nFib(n):
    a = 0
    b = 1
    result = list()
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    result.append(0)
    result.append(1)
    for i in range(0,n-2):
        result.append(result[-1]+result[-2])
    return result