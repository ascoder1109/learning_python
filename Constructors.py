class Person:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = Person("Aditya","SDE")
a.info()