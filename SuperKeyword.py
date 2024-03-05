class ParentClass:
    def parent_method(self):
        print("This is parent method")

class ChildClass(ParentClass):
    def parent_method(self):
        super().parent_method()

c = ChildClass()
c.parent_method();