def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Above function can also be imported!
    # from random_dictionary_words import get_words

# Markov chain- mathematical object, a bunch of states linked together

# Learn Markov Chain from corpus (how often does a token appear after another token?)

# Do a random walk on Markov Chain (pick a way to store it )


def markov_walk():
    markov_dictionary = {}
    # starts from some state, pick random transision, follow it, and repeat


# Make a sentence
def make_sentence(markov_dictionary):
