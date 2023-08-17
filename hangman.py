# Import elements & libraries
import random
import string
from words import words_list

# Random selection of valid word from words_list's dataset
def get_valid_word(words_list):
    random_word = random.choice(words_list) #Randomly chooses something from the list
    
    # If the word contains spaces or "-", keep searching for another word.
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words_list)
    return random_word.upper()


def hangman():
    target_word = get_valid_word(words_list) 
    target_word_letters = set(target_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #Empty set for the burnt letters
    
    # Get users input
    user_bet = input("Guess a letter").upper()
    if(user_bet in alphabet - used_letters):
        used_letters.add(user_bet)
        target_word_letters.remove(user_bet)
    elif(user_bet in used_letters):
        print("This letter is already used. Try again.")
    else:
        print("Invalid value. Try again.")
    
    #print(target_word, target_word_letters) 
    



hangman()