class Animal: #Parent Class (super class)
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Speaking Now...")

class Dog(Animal):
    def speak(self):
        super().speak() # super - we are useing the speak func of super class(parent class)
        print("Bhow Bhow!!")

# d=Dog("Bruno")
# d.speak()
Dog("Bruno").speak()