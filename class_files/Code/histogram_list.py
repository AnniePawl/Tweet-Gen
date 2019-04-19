
def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Above function can also be imported!
    # from random_dictionary_words import get_words


def histogram_list(word_list):
    """ Takes in source text, returns histogram data structure that stores unique words and their number of occurances as a list of lists """
    # Initialize (big)list to hold (baby)lists with type and count
    big_list = []
    for word in word_list:
        # Look for duplicate types so count can be increased instead of adding a whole new babylist
        for baby_list in big_list:
            if word == baby_list[0]:
                baby_list[1] += 1
                break  # stop iterating if you come across word
        else:
            list_to_append = [word, 1]
            big_list.append(list_to_append)
    return big_list


word_list = get_words("sample_text.txt")
print(histogram_list(word_list))
