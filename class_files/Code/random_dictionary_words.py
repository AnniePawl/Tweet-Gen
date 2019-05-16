import sys
import random

# Program accepts one argument (# of words)
# number = input("Enter a number: ")


def get_words(sample_text):
    """ reads file, strips leading and trailer characters, returns list of stings (#TODO?) """
    words = []
    with open("sample_text.txt") as f:  # closes file when done
        sample_text = f.read().strip().split(" ")
        return sample_text


def random_sentence(words):
    """ randomly selects words from list and returns them as a properly formatted sentence (#TODO array?) """
    random_words = random.choice(words)
    random_sentence = ' '.join(random_words)  # format sentence
    return random_sentence


if __name__ == '__main__':
    source = get_words('sample_text.txt')
    print(random_sentence(source))
