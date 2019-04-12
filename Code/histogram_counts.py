
def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Above function can also be imported!
    # from random_dictionary_words import get_words


def histogram_counts():
    """ Takes in source text, returns histogram data structure that stores number of occurances followed by all words with that number of occurances"""
