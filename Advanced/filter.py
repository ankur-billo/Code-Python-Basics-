#it doesn't print it just filter out the things which meet the requirementsS
def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
mubt=[1,3,6,7,8,9,34]
new = list(filter(is_greater_than_9,mubt))
print(new)  
