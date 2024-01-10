try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")
finally:
    print("I am final block")
    

    

