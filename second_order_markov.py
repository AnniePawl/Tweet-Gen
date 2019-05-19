from pprint import pprint
from random_dictionary_words import get_words
from stochastic import sample_by_frequency
from dictogram import Dictogram
# from cleaner import formatted_words_array
import random


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


def second_order_markov_sentence(markov_dictionary):
    """Start from some state, pick random transition, and generate a sentence based on relative probability"""
    # Choose start word at random from markov chain keys
    start_words = random.choice(list(markov_dictionary.keys()))
    word_list = []  # O(1)
    word_list.append(start_words)
    print(word_list)
    last_words = start_words
    for word in range(0, 20):
        # get historgram of all words following start word
        histogram = markov_dictionary[last_words]
        # use histogram to sample next word
        next_word = sample_by_frequency(histogram)
        # add new random word into words list
        word_list.append(next_word)
        # reassign last word so when loop starts again, you start from new word
        last_words = (last_words[1], next_word)

    random_sentence = ' '.join(word_list) + '.'
    return random_sentence


if __name__ == "__main__":
    # create a word_list
    word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    markov_dictionary = make_second_order_chain(word_list)
    pprint(markov_dictionary)
    pprint(second_order_markov_sentence(markov_dictionary))
