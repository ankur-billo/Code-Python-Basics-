class NegativeNumberError(Exception): #custom error exception is created-5
    
    pass
    
try:
    a=int(input("Enter the number: "))
    if a<0:
        raise NegativeNumberError("No Can't be Negative") # this thing shows up as terinal error
    result=45/a
    print(f"THe result is {result}")
    
except ValueError:
    print("Error! The input is not a Number!")
    
except ZeroDivisionError:
    print("Error! Don't divide by Zero!")