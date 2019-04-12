def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings (#TODO?) """
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words


def dictionary_histogram(word_list):  # sample text list
    histo_dict = {}
    for word in word_list:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word] = 1
    return histo_dict


sample_list = get_words("sample_text.txt")
print(tuple_dict(sample_list))
