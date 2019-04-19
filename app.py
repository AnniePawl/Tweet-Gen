from flask import Flask
from stochastic import sample_by_frequency, histogram

HTML = """<html>
<h1>Greetings Grasshopper</h1>
<h2>I'm about to birth a <h2>
<h3>{}</h3>
</html> """

app = Flask(__name__)


@app.route('/')
def random_bugs():
    """ Returns a random bug """
    bugs = histogram('spider ant butterfly'.split())
    random_bug = sample_by_frequency(bugs)
    return HTML.format(random_bug)
