from random_dictionary_words import get_words
from dictogram import Dictogram


def make_markov_chain(word_list):
    """Build a first-order markov chain from word_list"""
    markov_dictionary = {}  # O(1)
    for index in range(len(word_list)-1):  # O(n)
        current_word = word_list[index]  # O(1)
        next_word = word_list[index + 1]  # O(1)
        # If key already exists in markov, call add_count method from dictogram class to increase token count
        if current_word in markov_dictionary:
            markov_dictionary[current_word].add_count(next_word)
        # If not, create instance of dictogram object
        else:
            # Make sure to pass in list
            markov_dictionary[current_word] = Dictogram([next_word])
    return markov_dictionary  # O(1)

# Start at random word


def first_order_markov_sentence(markov_dictionary):
    """Start from some state, pick random transition, and generate a sentence based on relative probability"""
    sentence = []  # O(1)
    # start word = ?
    # next word based on histogram of start word

    random_sentence = ' ' + next_word
    # return random_sentence


# def test_markov_chain():
#     # create a word_list
#     word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
#     # create instance of Markov_Chain object
#     markov_chain = Markov_Chain(word_list)
#     # call make_chain on our Markov_Chain object
#     markov_object = markov_chain.make_chain(word_list)
#     # print the output
#     print(markov_object)
if __name__ == "__main__":
    # create a word_list
    word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    print(make_markov_chain(word_list))
