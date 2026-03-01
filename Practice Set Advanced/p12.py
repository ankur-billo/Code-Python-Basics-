def sum_all(*args):
    sum=0
    for item in args:
        sum+=item
    
    return sum
    
print(sum_all(5,7,8))