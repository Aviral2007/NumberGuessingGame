import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0

print("Guess a number Between 1 & 9")

while chances < 5:
    guess = int(input("Enter Your Guess : "))

    if guess == number:
        print("Congratulations You Won !!!")

    elif guess < number:
        print("Your Guess was too low, Guess higher than", guess)
        
    else:
        print("Your Guess was too high, Guess a lower number than", number)

if not chances < 5:
    print("You Lose !! The number is :", number)
