class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f"The name of employee {self.id} is {self.name}")
        

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e = Employee("Rohan",400)
e.showDetails()

p = Programmer("Aditya",500)
p.showDetails()