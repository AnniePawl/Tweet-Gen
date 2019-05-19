from flask import Flask
from stochastic import sample_by_frequency, histogram
from first_order_markov import make_first_order_chain, first_order_markov_sentence
from second_order_markov import make_second_order_chain, second_order_markov_sentence

HTML = """<html>
<h1>Greetings Grasshopper</h1>
<h2>I'm about to birth a <h2>
<h3>{}</h3>
</html> """

app = Flask(__name__)


@app.route('/')
def first_order_sentence_builder():
    return HTML.format(first_order_markov_sentence(make_first_order_chain)(words_array))


def second_order_sentence_builder():
    return HTML.format(second_order_markov_sentence(make_second_order_chain(words_array)))

# TEST


def random_bugs():
    """ Returns a random bug """
    bugs = histogram('spider ant butterfly'.split())
    random_bug = sample_by_frequency(bugs, 3)
    return HTML.format(random_bug)
