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


def dictionary_histogram(word_list):  # sample text list
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


# print(word_counts(sample_list))


# Creating a function (word_counts) - pass in words_list
# Initialize (big)list to hold lists(baby) with type and count
# Iterate over word_list (for loop)
# Look for ducplicate types
# - if duplicate, increase count by 1,
#  if not, add a new type with count of one

def tuple_dict(word_list):
    outer_list = []
    # found = False
    for word in word_list:
        current_tuple = (word, 1)
        for element in outer_list:
            print("cheese")
            if word == current_tuple[0]:
                new_tuple = current_tuple[1] + 1
                del current_tuple
                outer_list.append(new_tuple)
                break
            else:
                outer_list.append(current_tuple)
    return outer_list


def list_count(word_list):
    big_list = []
    for word in word_list:
        for baby_tuple in big_list:
            if word == baby_tuple[0]:
                count = baby_tuple[1]
                new_tuple = (word, count+1)
                # remove the old tuple
                big_list.remove(baby_tuple)

                # add the new tuple to big list
                big_list.append(new_tuple)

                # stop iterating if you come across word
                break
        # If we dont come across word, add word
        else:
            tuple_to_append = (word, 1)
            big_list.append(tuple_to_append)
    return big_list


word_list = get_words('fish.txt')
counts = list_count(word_list)
print(counts)

# for current_tuple in big_list:
#     if word == tuple_dict[0]:
#         # varaible to hold new value (increment by 1)
#         new_tuple_count = current_tuple[1] += 1
#         # delete old tuple  (del keyword)
#         del current_tuple[index]
# create new tuple -- word [0], [1] (variable)


sample_list = get_words("sample_text.txt")
print(tuple_dict(sample_list))
