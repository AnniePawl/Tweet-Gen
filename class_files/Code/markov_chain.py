# reads file, returns nice list of strings
from random_dictionary_words import get_words


class Markov_Chain(dict):
    def __init__(self.word_list):
        self.word_list = word_list

        self.tokens = 0  # number of occurances
        self.types = 0  # number of unique words

        if word_list is not None:  # create markov chain if word list has words
            self.make_chain(word_list)

    def make_chain(self, word_list):
        """Build Markov chain from word_list"""
        for index in range(len(self.word_list)-1)
        current_word = self.word_list[index]
        next_word = self.word_list[index + 1]
        if current_word in self:
            if next_word


def markov_chain_walk():
    markov_dictionary = {}  # store in dictionary
    # starts from some state, pick random transision, follow it, and repeat


# Make a sentence
def make_sentence(markov_dictionary):
