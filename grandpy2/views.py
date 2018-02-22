from flask import Flask, render_template, url_for, request, json

from grandpy2.quotes import *

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    if "search_location" in request.args:
        research_location = request.args.get("search_location")
        displayed_quote = research()
        displayed_quote.search(research_location)
        quote = displayed_quote.page_py.content[:500]

    else:
        quote = ""


    return render_template('index.html',
                           quote=quote)

