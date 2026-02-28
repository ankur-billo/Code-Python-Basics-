class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @property #makes the first_name a property using decorator
    def first_name(self):
        l= self.name.split(" ") #splits using space
        return l[0] #returns 1st name coz 0
    
    @first_name.setter
    def first_name(self,first):
        l= self.name.split(" ") #splits using space
        new_name=f"{first} {l[1]}"
        self.name=new_name
        
    
e = Employee("Rahul Shah", 5600)

# print(e.firs_name()) #if property not use
print(e.first_name) #if property use
e.first_name = "Joh"
print(e.name)