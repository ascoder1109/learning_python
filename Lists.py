marks= [67,45,89,44,33,22,11]
print(marks)
print(marks[1])
if 44 in marks:
    print("Yes its there")
else:
    print("No its not there")

anotherList = [i*i for i in range(100)if i%2==0]
print(anotherList)