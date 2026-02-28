a=int(input("Enter 1st no.: "))
b=int(input("Enter 1st no.: "))
try:
    print(f"The sum is {a+b}")  
except Exception as e:
    print(e)
    
finally: #this part is always execute irrespective of error or error free program
    print("This is always executed")