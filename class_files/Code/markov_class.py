class Markov_Chain(dict):
    def __init__(self, word_list):
        super(Markov_Chain, self).__init__()

        self.word_list = word_list  # O(1) to assign
        self.tokens = 0  # number of occurances, O(1) to assign
        self.types = 0  # number of unique words, O(1) to assign

        if word_list is not None:  # O(1) to check if list is  empty
            self.make_chain(word_list)
