
def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Above function can also be imported!
    # from random_dictionary_words import get_words


def dictionary_histogram(word_list):
    """ Takes in source text, returns histogram data structure that stores unique words and their number of occurances as a dictionary of key-value pairs """
    # Initialize an empty dictionary to hold word types and counts
    histo_dict = {}
    # First look for duplicate words(keys) and increase count (value) by one if found
    for word in word_list:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word] = 1
    return histo_dict


word_list = get_words("sample_text.txt")
print(dictionary_histogram(word_list))
