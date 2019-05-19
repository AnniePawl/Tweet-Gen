from flask import Flask
from stochastic import sample_by_frequency, histogram
from first_order_markov import make_first_order_chain, first_order_markov_sentence
from second_order_markov import make_second_order_chain, second_order_markov_sentence
from cleaner import formatted_words_array


app = Flask(__name__)


@app.route('/')
def first_order_sentence_builder():
    # sample_text = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    return HTML.format(first_order_markov_sentence(make_first_order_chain(formatted_words_array)))

  # def second_order_sentence_builder():
    # return HTML.format(second_order_markov_sentence(make_first_order_chain(formatted_words_array)))


HTML = """<html style="background: radial-gradient(circle at 75%, #333, #333, #616366 50%, #eee 50%, #5f6266 65%)";>
<h1 style="color:#5bd838; font-size: 70px; font-family: sans-serif">Hitchhiker's Guide to the Galaxy</br> Random Sentence Generator</h1>
<h3 style="color:white; font-size: 40px; font-family: sans-serif;">{}</h3>
<a href='/'><button style="font-weight:bold;background:#5bd838;height:50px;width:150px;border-radius:20px;">Generate a New Sentence</button></a>
</html> """
