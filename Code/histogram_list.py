def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings (#TODO?) """
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words


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
print(tuple_dict(sample_list))
