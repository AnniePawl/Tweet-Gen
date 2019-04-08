
def get_words(filename):
    """ Open file, return list of all words"""
    all_words_list = []
    with open(filename) as file:
        for line in file:
            words_list = line.split()
            for word in words_list:
                all_words_list.append(word)
    return all_words_list


def count_animal(animal_list):
    """count occurances in given list of animal and return data structure"""

    animal_counts = {}
    for animal_name in animal_list:
        # check is we've seen animal name before
        if animal_name in animal_counts:
            # increase occurance by one
            animal_counts[animal_name] += 1
        else:
            animal_counts[animal_name] = 1

    return animal_counts


def print_table(animal_counts):
    """Prints table of animals"""
    print('Animal | Count')
    print('--------------')
    for animal in animal_counts:
        print('{} | {}'.format(animal_name, count))
        animal_counts


# Get name and counts at same time during iteration
for animal_name, count in animal_counts.items:


animal_list = get_words('animals.txt')
counts = animal_counts('animal_list')
print(counts)
