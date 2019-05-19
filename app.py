from flask import Flask
from stochastic import sample_by_frequency, histogram
from first_order_markov import make_first_order_chain, first_order_markov_sentence
from second_order_markov import make_second_order_chain, second_order_markov_sentence
from cleaner import formatted_words_array

HTML = """<html>
<h1>Anna's Random Sentence Generator</h1>
<h2>MVP<h2>
<h3>{}</h3>
</html> """

app = Flask(__name__)


@app.route('/')
def first_order_sentence_builder():
    # sample_text = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    return HTML.format(first_order_markov_sentence(make_first_order_chain(formatted_words_array)))


if __name__ == "__main__":
    # create a word_list

    def second_order_sentence_builder():
        pass
        return HTML.format(second_order_markov_sentence(make_second_order_chain(words_array)))

    def random_bugs():
        pass
        """ For testing purposes: Returns a random bug """
        bugs = histogram('spider ant butterfly'.split())
        random_bug = sample_by_frequency(bugs)
        return HTML.format(random_bug)
