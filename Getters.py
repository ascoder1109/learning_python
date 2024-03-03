class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
        
    @property
    def tenValue(self):
        return 10*self._value
    

obj = MyClass(10)
print(obj.tenValue)
obj.show()