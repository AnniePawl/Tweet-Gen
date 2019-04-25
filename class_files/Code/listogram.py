#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Check words(stored at index 0),if you find duplicate word, increase count(tokens(stored atindex[1]) by one.
        is_updated = False
        for index, pair in enumerate(self):
            current_word, c = pair
            if current_word == word:
                # look into list alias, pair
                self[index][1] += count
                self.tokens += count
                is_updated = True
                break
        if is_updated == False:
            self.append([word, count])
            self.tokens += count
            self.types += 1
        print(self)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # Retrieve word frequency count
        # Check each word, if duplicate found, return count(stored at index 1)
        for index in range(len(self)):
            if self[index][0] == word:
                return self[index][1]
            # If word not found, return count (0)
            else:
                return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # Check if word is in this histogram, return True or False
        for index in range(len(self)):
            if self[index][0] == word:
                return True
            else:
                return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # Implement linear search to find index of entry with target word
        for index in range(len(self)):
            if self[index][0] == target:
                return index
            return None


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
