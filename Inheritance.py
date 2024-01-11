class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("Bark")
    # pass

class Cat(Mammal):
    def beAnnoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 =Cat()
cat1.beAnnoying()