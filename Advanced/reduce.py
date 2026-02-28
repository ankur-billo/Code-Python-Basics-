from functools import reduce

# def sum(a,b):
#     return a+b
num=[3,4,6,2]
#   [7,6,2]
#   [13,2]
#   [15]
c=reduce(lambda a,b: a+b,num)
print(c)