def sum(number, counter):
    if(number==0):
        return counter
    else:
        return sum(number-1,counter+number)
    
print(sum(6,0))