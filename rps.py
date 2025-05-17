import random

sign = ("Rock", "Paper", "Scissor")
user = None
user_point = 0
computer_point = 0

print("First one to win three rounds win")
print()

while user_point < 3 and computer_point < 3:
    user = input("Enter your choice(Rock/Paper/Scissor): ")
    computer = random.choice(sign)

    if computer == "Rock" and user == "Paper":
        print(f"You chose {user} and your opponent chose {computer}")
        print("You won this round")
        print()
        user_point += 1
    elif computer == "Rock" and user == "Scissor":
        print(f"You chose {user} and your opponent chose {computer}")
        print("Your opponent won this round")
        print()
        computer_point += 1
    elif computer == "Paper" and user == "Scissor":
        print(f"You chose {user} and your opponent chose {computer}")
        print("You won this round")
        print()
        user_point += 1
    elif computer == "Paper" and user == "Rock":
        print(f"You chose {user} and your opponent chose {computer}")
        print("Your opponent won this round")
        print()
        computer_point += 1
    elif computer == "Scissor" and user == "Rock":
        print(f"You chose {user} and your opponent chose {computer}")
        print("You won this round")
        print()
        user_point += 1
    elif computer == "Scissor" and user == "Paper":
        print(f"You chose {user} and your opponent chose {computer}")
        print("Your opponent won this round")
        print()
        computer_point += 1
    else:
        print("Draw!")

if user_point == 3:
    print("Congratulations!!! You won")
elif computer_point == 3:
    print("Your opponent won")
