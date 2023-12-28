list1 = [3,5,3,2,4,6,7,3,2,4,5]
isEven = bool(any(i%2==0 for i in list1))
isEvenAll = bool(all(i%2==0 for i in list1))
print(isEven)
print(isEvenAll)