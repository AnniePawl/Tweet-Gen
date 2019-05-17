from pprint import pprint
from random_dictionary_words import get_words
from dictogram import Dictogram
import random

# Consider start and stop tokens!


def make_second_order_chain(word_list):

    markov_dictionary = {}  # O(1)
    """Build a second-order markov chain from word_list"""
    for index in range(len(word_list)-2):
        # Current words held in tuple:
        current_words = (word_list[index], word_list[index+1])
        next_word = word_list[index + 2]

        # If key already exists in markov_dictionary, call add_count method from dictogram class to increase token count
        if current_words in markov_dictionary:
            markov_dictionary[current_words].add_count(next_word)
        # If key doesnt already exists, create instance of Dictogram object
        # Make sure to pass in list
        else:
            markov_dictionary[current_words] = Dictogram([next_word])
    return markov_dictionary  # O(1)
    # print(markov_dictionary)


def second_order_markov_sentence(markov_dictionary):
    """Start from some state, pick random transition, and generate a sentence based on relative probability"""
    words_list = []  # O(1)
    # Choose start word at random from markov chain keys
    start_word = random.choice(markov_dictionary.keys)

    # get historgram of all words following start word
    markov_dictionary[start_word]
    # use histogram to sample next word
    # next_word = markov_dictionary[start_word[]]
    # new random word into words list
    words_list.append(next_word)

    random_sentence = ' '.join(words_list) + '.'
    return random_sentence


if __name__ == "__main__":
    # create a word_list
    word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    cat_sentence = "I like cats and you like cats"
    cat_word_list = cat_sentence.split()
    pprint(make_second_order_chain(cat_word_list))
