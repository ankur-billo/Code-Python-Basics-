class employees:
    company="asus"
    
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond
    
    def get_salary(self):
        return self.salary
    
    def info(self):
        print(f"I {self.name} got {self.salary} for {self.bond}years")
    
e1 = employees(3400,"John",5)
print(e1.bond)
# Object Introspection
print(dir(e1))