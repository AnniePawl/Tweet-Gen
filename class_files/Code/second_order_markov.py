from random_dictionary_words import get_words
from dictogram import Dictogram


def make_chain(word_list):

    markov_dictionary = {}  # O(1)
    """Build a second-order markov chain from word_list"""
    for index in range(len(word_list)-1):
        current_word = word_list[index]
        next_word = word_list[index + 1]
        # If key already exists in markov_dictionary, call add_count method from dictogram class to increase token count
        if current_word in markov_dictionary:
            markov_dictionary[current_word].add_count(next_word)
        # If key doesnt already exists, create instance of Dictogram object
        # Make sure to pass in list
        else:
            markov_dictionary[current_word] = Dictogram([next_word])
    return markov_dictionary  # O(1)
    # print(markov_dictionary)


def second_order_markov_sentence(markov_dictionary):
    pass


if __name__ == "__main__":
    # create a word_list
    word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    print(make_chain(word_list))
