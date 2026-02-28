while True:
    try:
        a=int(input("Enter 1st no.: "))
        b=int(input("Enter 1st no.: "))
        print(f"The sum is {a+b}")
        
    # except: #just the error message
    #     print("Some errors happend!")
    
    except Exception as e: #the error message with the description of error
        print("Some errors happend!",e)