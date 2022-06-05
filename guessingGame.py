import random

print ("Number guessing game")
number = random.randint(1, 9)

chance = 0
guess=int(input("Make a guess: "))
print(guess)

while (chance < 5):
   if chance == number:
    print("Great guess! You won!")

if not chance < 5:
    print("The number was", number, "Better luck next time!")
