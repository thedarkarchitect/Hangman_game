from art import *
from game_data import *
import random
# print(logo)
# print(vs)

score = 0
person = random.choice(data)
person_B = random.choice(data)
should_continue = True

def compare_A():
    global score , person, person_B, should_continue
    if person['follower_count'] > person_B['follower_count']:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False

def compare_B():
    global score , person, person_B, should_continue
    
    if person_B['follower_count'] > person['follower_count']:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False


while should_continue:
    print(logo)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {person['name']}, a {person['description']}, from {person['country']}")

    print(vs)
    print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")

    if person == person_B:
        person_B = random.choice(data)

    option = input("Who has more followers? type 'A' or 'B': ")


    if option == "A" :
        compare_A()

    elif option == "B":
        compare_B()
    else:
        should_continue = False
        
    person = person_B
        
    person_B = random.choice(data)

