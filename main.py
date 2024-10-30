from random import randint

random_num = randint(1, 10)
game = True

while game:
    guess = int(input("Guess the number (between 1 and 10):"))
    if guess > random_num:
        print("Too high! Try again.")
    elif guess < random_num:
        print("Too low! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        game = False