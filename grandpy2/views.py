from flask import Flask, render_template, url_for, request, json

from grandpy2.quotes import *

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html', quote=quote)

@app.route('/geoloc')
def geoloc():
    location = request.args.get("location")
    adress = map()
    adress.search(location)
    locationAdress = adress.postalAdress
    return(locationAdress)



@app.route('/quote')
def quote():
    location = request.args.get("location")
    displayed_quote = research()
    displayed_quote.search(location)
    endQuote = displayed_quote.page_py.content[:200] + "..."
    return(endQuote)