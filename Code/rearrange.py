import sys
import random


def rearrange_words(input_words):
    rearranged_words = []

    while len(rearranged_words) < len(input_words):
        rand_index = random.randint(0, len(input_words) - 1)
        rand_word = input_words[rand_index]
        if rand_word in rearranged_words:
            continue
        rearranged_words.append(rand_word)

    result = ' '.join(rearranged_words)
    return result


if __name__ == '__main__':
    # remember arg 1 is file name
    input_words = sys.argv[1:]

    print(rearrange_words(input_words))
