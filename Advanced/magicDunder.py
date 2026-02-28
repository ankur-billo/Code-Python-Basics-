class Employee:
    company ="ASUS"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    #str is used by user mainly
    def __str__(self):
        return f"The name is {self.name} and the Salary is {self.salary}"
    
    #repr is used by developer to debug mainly
    def __repr__(self):
        return f"name: {self.name} /n salary: {self.salary}"
    
    #len is used for getting the length
    def __len__(self):
        return len(self.name)
    
e1= Employee("Hello",5000)
print(len(e1))