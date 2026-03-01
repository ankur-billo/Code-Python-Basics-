from functools import reduce
g=[1,2,3,4]
product=reduce(lambda a,b: a*b,g)
print(product)