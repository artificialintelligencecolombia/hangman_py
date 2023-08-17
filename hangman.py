# Import elements & libraries
import random
from words import words_list

# Random selection of valid word from words_list's dataset
def get_valid_word(words_list):
    random_word = random.choice(words_list) #Randomly chooses something from the list
    
    #if the word contains spaces or "-", keep searching for another word.
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words_list)
    return random_word.upper()

def hangman():
    target_word = get_valid_word(words_list) 
    target_word_letters = set(target_word)
    print(target_word, target_word_letters) 
    return target_word_letters



hangman()