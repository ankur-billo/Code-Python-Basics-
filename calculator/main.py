try:
    a=int(input("Enter the 1st no.: "))
    b=int(input("Enter the 2nd no.: "))
    print("Enter the operation you want to perform--\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")
    o=input("Enter the operation: ")
    match o:
        case "+" :
            print(f"The Result is {a+b}")
        case "-" :
            print(f"The Result is {a-b}")
        case "*" :
            print(f"The Result is {a*b}")
        case "/" :
            print(f"The Result is {a/b}")
        case default :
            print("There is an error!")
except Exception as e:
    print("Enter a valid number to perfrom",e)