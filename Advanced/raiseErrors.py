#handle errors without try except but raise

a=int(input("Enter 1st no.: "))
b=int(input("Enter 1st no.: "))
if (b==0):
    raise ValueError("Don't divide by 0")
print(f"The sum is {a+b}")