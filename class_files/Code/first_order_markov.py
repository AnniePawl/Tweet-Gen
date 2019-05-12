from random_dictionary_words import get_words
from dictogram import Dictogram


# class Markov_Chain(dict):
#     def __init__(self, word_list):
#         super(Markov_Chain, self).__init__()

#         self.word_list = word_list  # O(1) to assign
#         self.tokens = 0  # number of occurances, O(1) to assign
#         self.types = 0  # number of unique words, O(1) to assign

#         if word_list is not None:  # O(1) to check if list is  empty
#             self.make_chain(word_list)

def make_chain(word_list):

    markov = {}
    """Build Markov chain from word_list"""
    for index in range(len(word_list)-1):
        current_word = word_list[index]
        next_word = word_list[index + 1]
        # If key already exists in markov, call add_count method from dictogram class to increase token count
        if current_word in markov:
            markov[current_word].add_count(next_word)
        # If key doesnt already exists, create instance of Dictogram object
        # Make sure to pass in list
        else:
            markov[current_word] = Dictogram([next_word])
    return markov
    # print(markov)


def markov_walk():
    markov_dictionary = {}  # store in dictionary
    # starts from some state, pick random transision, follow it, and repeat


def make_sentence(markov_dictionary):
    pass


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

    print(make_chain(word_list))
