def sumOfDigits(n):
    if(n==0 or n==1):
        return n
    return n%10+sumOfDigits(n//10)
print(sumOfDigits(10))