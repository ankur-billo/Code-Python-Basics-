class MathUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a utility  class for")

# #using OBJECT
# a=MathUtils
# print(a.add(5,6))
# a.description()

#without OBJECT
MathUtils.description()
print(MathUtils.add(4,5))