def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings (#TODO?) """
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words

# Creating a function (word_counts) - pass in words_list
# Initialize dictionary to hold Types and Counts
# Iterate over list (for loop)
# Look for ducplicate keys - if duplicate, increase count by 1, if not, add a new kew with count of one
#

# Dictionary Histogram


def word_counts(word_list):  # sample text list
    histo_dict = {}
    for word in word_list:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word] = 1
    return histo_dict


# Creating a function (word_counts) - pass in words_list
# Initialize (big)list to hold lists(baby) with type and count
# Iterate over word_list (for loop)
# Look for ducplicate types
# - if duplicate, increase count by 1,
#  if not, add a new type with count of one


def list_count(word_list):
    big_list = []
    for word in word_list:
        for baby_list in big_list:
            if word == baby_list[0]:
                baby_list[1] += 1
                # stop iterating if you come across word
                break
        # If we dont come across word, add word
        else:
            list_to_append = [word, 1]
            big_list.append(list_to_append)
    return big_list


sample_list = get_words("sample_text.txt")
print(list_count(sample_list))

# print(word_counts(sample_list))


# Creating a function (word_counts) - pass in words_list
# Initialize (big)list to hold lists(baby) with type and count
# Iterate over word_list (for loop)
# Look for ducplicate types
# - if duplicate, increase count by 1,
#  if not, add a new type with count of one

def tuple(word_list):
    dict_tuple = ()
    for word in word_list:
