import random
userChoice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computerChoice = random.randint(0,2)
# print(f"Computer choose {computerChoice}")
if (userChoice>=3 or userChoice<0):
    print("You typed an Invalid number, you lose!")
elif (userChoice == 0 and computerChoice ==2):
    print("You Win")
elif (computerChoice == 0 and userChoice ==2):
    print("You lose")
elif(computerChoice>userChoice):
    print("You Lose")
elif(userChoice>computerChoice):
    print("You win!")
elif(computerChoice==userChoice):
    print("Draw!")
