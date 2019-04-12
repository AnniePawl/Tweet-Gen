from flask import Flask
from stochastic import sample_by_frequency


HTML = """<html>
<h1>Greetings Grasshopper</h1>
<h3>{}</h3>
</html> """

app = Flask(__name__)


@app.route('/')
def hello_world():
    bugs = 'spider ant butterfly'.split()
    random_bug = sample_by_frequency(bugs)
    return HTML.format(random_bug)
