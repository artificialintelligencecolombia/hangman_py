# Import elements & libraries
import random
from words import words_list

# Random selection of VALID words

def get_valid_word(words_list):
    random_word = random.choice(words_list)
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words_list)
    return random_word

print(get_valid_word(words_list)) 