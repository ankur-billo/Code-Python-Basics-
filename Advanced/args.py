def sum(*args):
    #args will be a tuple for all the values passed to
    total=0
    for item in args:
        total+=item
    return total
print(sum(1,23,4))