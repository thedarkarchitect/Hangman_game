from art import logo
from random import randint

def game():
    global number, lives
    should_continue  = True
    while should_continue:
        print(f"You have {lives} remaining")
        guess = int(input("Make a guess: "))

        if guess > number:

            
            print("Too high.")
            print("Guess again.")
            lives -= 1
        elif guess < number:
            
            print("Too low.")
            print("Guess again.")
            lives -= 1
        elif guess == number:
            print(f"You have {lives} remaining")
            print("You WIN.")
            should_continue = False

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
number = randint(1,100)
lives = 5
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ") 

if difficulty == "easy":
    lives += 5
    game()
    
elif difficulty == "hard":
    game()


