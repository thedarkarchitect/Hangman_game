
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]


import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#This control the chances of the game
lives = 6

print(chosen_word)

display = []

for _ in chosen_word:
  display.append("_")

print(display)

while not end_of_game :
    print(stages[lives])
    print(lives)
    guess = input("Make a guess: ").lower()

    #We use the range of the chosen word to make an index that works for both the chosen word and the display
    for position in range(len(chosen_word)):
        
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    
    if guess not in chosen_word:
        lives = lives - 1
            
    if lives == 0:
        print(stages[lives])
        end_of_game = True
        print("You lose")

    #tHIS Turns all elements in the display list to a string
    print(f"{' '.join(display)}")

    if  "_" not in display:
        end_of_game = True
        print("You win.")
            

