class Employee:
    def __init__(self):
        self.__name = "Aditya"
        
a = Employee()
# print(a.__name) Cannot be accessed directly
print(a._Employee__name)