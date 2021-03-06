def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings"""
    words = []
    with open(sample_text) as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text  # this is a list of words


def animal_counts_histogram(animal_list):
    """Takes in source text (list of animals) and returns unique words and their number of occurances as key-value paurs  """
    # Initiate empty dictiaonry to hold unique words as keys and number of occurances and values
    animal_counts_dictionary = {}
    for animal_name in animal_list:
        if animal_name in animal_counts_dictionary:
            animal_counts_dictionary[animal_name] += 1
        else:
            animal_counts_dictionary[animal_name] = 1
    return animal_counts_dictionary


def print_pretty_table(animal_counts_histogram):
    """ Returns animal historgram in a pretty table format """
    print('Animal | Count')
    print('--------------')
    for animal_name in animal_counts_dictionary:
        print('{} | {}'.format(animal_name, count))


animal_list = get_words('animals.txt')
print(animal_counts_histogram(animal_list))
print(print_pretty_table(animal_counts_histogram))


def find_animals_mvp():
    def is_animals(animal):
        if animal.startswith('t'):
            return True


def find_animals():
    return animal


condition = animal.startswith('t')


current_node = self.head
# Loop until Node is None
while current_node is not None:
    # Check if node's data satisfies quality
    if quality(curret_node.data):
        # return data that satisfies quality
        return current_node.data
    else:  # otherwise skip to next node
        current_node = current_node.next
