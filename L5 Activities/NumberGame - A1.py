import random

number = random.randint(0, 9)

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
print("Give me your best guess!")

guess = int(input())

if guess == number:
    print("Hero! You guessed the correct number.")
else:
    print("Oops! The number was", number)