import sys


def reverse_sentence(input_sentence):
    reversed_sentence = input_sentence[::-1]
    return (" ".join(reversed_sentence))


def reverse_word(input_word):
    reversed_word = input_word[::-1]
    return reversed_word


def reverse_both


if __name__ == '__main__':
    # input_sentence = sys.argv[1:]
    # print(reverse_sentence(input_sentence))

    input_word = sys.argv[1]
    print(reverse_word(input_word))

 # [start:stop:step]
