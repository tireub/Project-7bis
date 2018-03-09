from flask import Flask, render_template, url_for, request, json

from grandpy2.quotes import *

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html', quote=quote)


@app.route('/parse')
def parse():
    location = request.args.get("location")
    parsed_location = parser()
    parsed_location.reject_useless_info(location)
    return (parsed_location.result)


@app.route('/geoloc')
def geoloc():
    location = request.args.get("location")
    address = map()
    address.search(location)
    locationAddress = address.postalAddress
    return(locationAddress)


@app.route('/quote')
def quote():
    location = request.args.get("location")
    displayed_quote = research()
    displayed_quote.search(location)
    endQuote = displayed_quote.page_py
    return(endQuote)
