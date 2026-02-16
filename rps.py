
import random

choices = ['rock', 'paper', 'scissors']

while True:
    user = input("Rock, Paper, Scissors? ")  
    if user not in choices:
        print("Invalid input!")
        continue
    comp = random.choice(choices)
    print("Computer chose:", comp)

    if user == comp:
        print("Tie!")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    if input("Play again? (y/n): ") == 'n': 
        break
print("Bye!")
