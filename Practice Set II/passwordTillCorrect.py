password = "Y2k123"
entered_pass=input("Enter your password: ")
while(entered_pass != password):
    entered_pass=input("Wrong Password! Try Again !\nEnter your password: ")
print("Successfully Logged In!")