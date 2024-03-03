x = 10 #global variable
def myFunction():
    global x
    y = 5
    print(x)
    print(y)
    
myFunction()