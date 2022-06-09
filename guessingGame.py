import random

print ("Number guessing game")
number = random.randint(1, 9)

chance = 0

while chance <5:
    guess=int(input("Make a guess between 1 to 9: "))

    if guess == number:
        print("Great guess! You won!")
        break
    elif guess < number:
        print("Your guess is lesser than the number", guess)
    else:
        print("Your guess is greater than your number", guess)
    
    chance=chance+1
    
if not chance < 5:
    print("The number was", number, "Better luck next time!")