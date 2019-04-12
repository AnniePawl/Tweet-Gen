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
