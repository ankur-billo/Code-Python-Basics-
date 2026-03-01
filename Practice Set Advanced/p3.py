class Employee:
    def __init__(self,salary):
        self._salary=salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if(value<0):
            print("Don't enter a negative number!")
        else:
            self._salary=value
        
    
e=Employee(234)
print(e.salary)
e.salary=45
print(e.salary)