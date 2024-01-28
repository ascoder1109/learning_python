import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timeInHours = int(time.strftime("%H"))
if(timeInHours>=8):
    print("Good Morning")
elif(timeInHours>=2):
    print("Good Afternoon")
elif(timeInHours>=5):
    print("Good Evening")
elif(timeInHours>=9):
    print("Good Night")