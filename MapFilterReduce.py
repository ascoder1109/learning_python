from functools import reduce

cube = lambda x : x*x*x;
l = [1,2,3,4,5,6,7]
newl = list(map(cube,l))
print(newl)

# filter
def filterFunction(a):
    return a>4

newnewL = list(filter(filterFunction,l))
print(newnewL)

#reduce
numbers = [1,2,3,4,5,6]
sum = reduce(lambda x ,y : x+y,numbers)
print(sum)
