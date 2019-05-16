import random


# CREATE a DICTIONARY of WORDS
def histogram(phrase):
    """Returns unique values and the number of occurances of each"""
    dict_histogram = {}
    for word in phrase:
        if word not in dict_histogram:
            dict_histogram[word] = 1
        else:
            dict_histogram[word] += 1
    return dict_histogram


def sample_by_frequency(dict_histogram):
    """ Returns a random word selected based on relative probability """
    total_tokens = sum(dict_histogram.values())
    random_num = random.uniform(0, total_tokens)
    num = 0
    for word in dict_histogram:
        count = dict_histogram[word]
        num += count
        if num > random_num:
            return word


if __name__ == '__main__':
    phrase = histogram("one fish two fish red fish blue fish".split(" "))
    sample_list = 'spider ant butterfly'.split()
    bugs = histogram(sample_list)
    # print(phrase)
    # Try Sum Function - Store once and hold in variable b/c total tokens will remain the same
    words = []
    for _ in range(0, 100000):
        words.append(sample_by_frequency(phrase))
    # print(words)

    print(histogram(words))
