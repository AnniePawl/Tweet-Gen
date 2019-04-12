
def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Above function can also be imported!
    # from random_dictionary_words import get_words


def histogram_tuple(word_list):
    """ Takes in source text, returns histogram data structure that stores unique words and their number of occurances as a list of tuples """
    outer_list = []
    for word in word_list:
        for baby_tuple in outer_list:
            if word == baby_tuple[0]:
                count = baby_tuple[1]
                # varaible to hold new tuple b/c old tuple can't be modified
                new_tuple = (word, count+1)
                # remove old tuple b/c it's count is inaccurate now
                outer_list.remove(baby_tuple)
                outer_list.append(new_tuple)
                break  # stop iterating if you come across word
        else:
            tuple_to_append = (word, 1)
            outer_list.append(tuple_to_append)
    return outer_list


word_list = get_words('sample_text.txt')
print(histogram_tuple(word_list))
