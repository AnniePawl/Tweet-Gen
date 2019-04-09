import sys


def is_it_an_anangram(input1, input2):
    """checks to see if two inputs are anagrams"""
    sorted_word1 = sorted(input1)
    sorted_word2 = sorted(input2)

    if sorted_word1 == sorted_word2:
        print("Yipee, these words are anagrams!")
    else:
        print("Hate to break it to ya, no anagram here")
    # return (do I need return here?)


if __name__ == '__main__':
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    print(is_it_an_anangram(input1, input2))
    # why is None being printed ?
