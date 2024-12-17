# Built-in module
import random

# Function to check teh winner.
def check(com, user):
    if (com == user):
        return 0
    elif (com == 0) and (user == 1):
        return 1
    elif (com == 0) and (user == 2):
        return 2
    elif (com == 1) and (user == 0):
        return 2
    elif (com == 1) and (user == 2):
        return 1
    elif (com == 2) and (user == 0):
        return 1
    elif (com == 2) and (user == 1):
        return 2
    else:
        raise ValueError ("VALUE ERROR !!!")

while True:
    # taking input.
    com = random.randint(0,2)
    user = int(input("Enter the numeric value of rock, paper and sissior [rock = 0, paper = 1, sissor = 2]\n=>"))
# printing what computer has chosen.
    if (com == 0):
        print("\ncom = rock")
    elif (com == 1):
        print("\ncom = paper")
    else:
        print("\ncom = sissor")
# printing what user has chosen.
    if (user == 0):
        print("user = rock\n")
    elif (user == 1):
        print("user = paper\n")
    else:
        print("user = sissor\n")

    score = check(com, user)
# printing final result.
    if (score == 0):
        print("Its a draw, try again !\n")
    elif(score == 1):
        print("Congratulations, you've won !\n")
    else:
        print("You've lost, try again !\n")

