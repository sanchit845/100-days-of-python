'''
rock = -1
paper = 1
scissors = 0
'''

import random


computer = random.choice([-1, 0, 1])
you = input("Enter your choice (rock (r), paper (p), scissors (s)): ").lower()
yourdict = {'r': -1, 'p': 1, 's': 0}
your = yourdict[you]

if computer == -1 and your == 1:
    print("You win! Paper beats rock.")
elif computer == -1 and your == 0:
    print("You lose! Rock beats scissors.")
elif computer == 1 and your == -1:
    print("You lose! Paper beats rock.")
elif computer == 1 and your == 0:
    print("You win! Scissors beats paper.")
elif computer == 0 and your == -1:
    print("You win! Rock beats scissors.")
elif computer == 0 and your == 1:
    print("You lose! Scissors beats paper.")
elif computer == your:
    print("It's a tie!")
else:
    print("Invalid input. Please enter 'r', 'p', or 's'.")

print(f"Computer chose: {'rock' if computer == -1 else 'paper' if computer == 1 else 'scissors'}")