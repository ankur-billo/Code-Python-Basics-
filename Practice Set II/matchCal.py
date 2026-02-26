a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
op = input("Enter the operation to be performed: ")
match op:
    case "+" :
        print(a,"+",b,"=",a+b)
    case "-" :
        print(a,"-",b,"=",a-b)
    case "/" :
        print(a,"/",b,"=",a/b)
    case "*" :
        print(a,"*",b,"=",a*b)
    case _:
        print("Wrong Input!")
        