from random_dictionary_words import get_words
from dictogram import Dictogram


class Markov_Chain(dict):
    def __init__(self, word_list):
        super(Markov_Chain, self).__init__()

        self.word_list = word_list
        self.tokens = 0  # number of occurances, O(1) to assign
        self.types = 0  # number of unique words, O(1) to assign

        if word_list is not None:  # O(1) to check if list is  empty
            self.make_chain(word_list)

    def make_chain(self, word_list):
        """Build Markov chain from word_list"""
        for index in range(len(self.word_list)-1):
            current_word = self.word_list[index]
            previous_word = self.word_list[index - 1]

            if previous_word is None:

    def markov_walk():
        markov_dictionary = {}  # store in dictionary
        # starts from some state, pick random transision, follow it, and repeat

    # Make a sentence
    def make_sentence(markov_dictionary):
