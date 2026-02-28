class Employee:
    company = "HP"
    def __init__(self,name,salary): #constructor
        self.name=name
        self.salary=salary
        
    #Instance Method(default) - any method inside class is by default instance method
    def print_info(self):
        info =f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    
    #Static Method - doesn't require self
    @staticmethod
    def sum(a,b):
        return a+b
    
    #Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)
        
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
        
e1 = Employee("Ram",5600)
e2 = Employee("Sam",6900)
e1.print_info()
e2.print_info()
print(e2.sum(5,6))
print(Employee.company)
e1.change_company("Lool")
print(Employee.company)
