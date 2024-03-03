class Person:
    name = "Aditya"
    occupation = "Software Engineer"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
# a.name = "Subham"
# a.occupation = "Accountant"
print(a.name,a.occupation)
a.info()