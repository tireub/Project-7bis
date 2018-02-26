from flask import Flask, render_template, url_for, request, json

from grandpy2.quotes import *

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html', quote=quote)

def quote(location):
    displayed_quote = research()
    displayed_quote.search(location)
    quote = displayed_quote.page_py.content[:200] + "..."
    return(quote)