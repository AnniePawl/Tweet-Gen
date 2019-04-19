import sys
import random


def rearrange_words(input_words):
    """Randomly rearranges a set of words provided as commandline arguments"""
    # Initiate new list to hold rearranged words
    rearranged_words = []
    # Randomly place input words in rearranged_words list until all input words are used
    while len(rearranged_words) < len(input_words):
        rand_index = random.randint(0, len(input_words) - 1)
        rand_word = input_words[rand_index]
        # Skip words that have already been seen
        if rand_word in rearranged_words:
            continue
        rearranged_words.append(rand_word)

    # Turn list into a nicely formatted string
    result = ' '.join(rearranged_words)
    return result


if __name__ == '__main__':
    # remember argument one is file name!
    input_words = sys.argv[1:]
    print(rearrange_words(input_words))
