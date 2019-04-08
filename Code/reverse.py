import sys


def reverse_sentence(input_sentence):
    """Returns sentence in reverse order"""
    reversed_sentence = input_sentence[::-1]
    return reversed_sentence


def reverse_word(input_word):
    """Returns word in reverse order"""
    reversed_word = input_word[::-1]
    return reversed_word


def reverse_reverse(input):
    """Returns words AND sentence in reverse order"""
    # Call reverse_sentence func, put words in new variable (type list)
    reverse_input = reverse_sentence(input)
    # Initialize new list to hold reversed newly words
    reverse_list = []
    # Iterate over each word in list, call reverse_word func
    for word in reverse_input:
        backwards_word = reverse_word(word)
        reverse_list.append(backwards_word)
    return " ".join(reverse_list)


if __name__ == '__main__':
    # input_word = sys.argv[1:]
    # print(reverse_word(input_word))

    # input_sentence = sys.argv[1:]
    # print(reverse_sentence(input_sentence))

    input = sys.argv[1:]
    print(reverse_reverse(input))
