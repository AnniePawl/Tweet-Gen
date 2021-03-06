from random_dictionary_words import get_words
from dictogram import Dictogram


class Markov_Chain(dict):
    def __init__(self, word_list):
        super(Markov_Chain, self).__init__()

        self.word_list = word_list  # O(1) to assign
        self.tokens = 0  # number of occurances, O(1) to assign
        self.types = 0  # number of unique words, O(1) to assign

        if word_list is not None:  # O(1) to check if list is  empty
            self.make_first_order_chain(word_list)

    def make_first_order_chain(word_list):
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

    def first_order_markov_sentence(markov_dictionary):
        """Start from some state, pick random transition, and generate a sentence based on relative probability"""
        words_list = []  # O(1)
        # Choose start word at random from markov chain keys
        start_word = random.choice(list(markov_dictionary.keys()))
        words_list.append(start_word)

        last_word = start_word
        for word in range(0, 10):
            # get historgram of all words following start word
            histogram = markov_dictionary[last_word]
            # use histogram to sample next word
            next_word = sample_by_frequency(histogram)
            # add new random word into words list
            words_list.append(next_word)
            # reassign last word so when loop starts again, you start from new word
            last_word = next_word

        random_sentence = ' '.join(words_list) + '.'
        return random_sentence
