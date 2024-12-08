import random

Min_value = 0
Max_value = 100
# Generate a random number between Min_value and Max_value
random_number = random.randint(Min_value,Max_value)
isRunning = True
guesses = 0

while isRunning :
    guess = input("Enter your Guess : ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if(guess < Min_value or guess > Max_value):
            print("Please enter a number between", Min_value, "and", Max_value)
        elif (guess < random_number):
            print("Too low, try a higher number")
        elif(guess > random_number):
            print("Too high, try a lower number")
        else:
            print("Congratulations, you have guessed the number in", guesses, "guesses")
            isRunning = False
    else:
        print(f"Invalid Input , Please enter a number between {Min_value} and {Max_value}")
