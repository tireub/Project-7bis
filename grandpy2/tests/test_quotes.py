from grandpy2 import quotes as quote

import requests


def test_init():
    location = quote.research()
    assert location.page_py == ""

def test_abstract():
    location = quote.research()
    location.search("Openclassrooms")
    assert location.page_py == "OpenClassrooms est une école en ligne. " \
                               "Chaque visiteur peut à la fois être un lecteur" \
                               " ou un rédacteur. Les cours peuvent être" \
                               " réalisés aussi bien par des membres, " \
                               "par l'équipe du site, ou éventuellement " \
                               "par des professeurs d'universités ou de" \
                               " grandes écoles partenaires."

def test_address():
    adress = quote.map()
    adress.search("openclassrooms")
    assert adress.postalAddress == "7 Cité Paradis, 75010 Paris, France"


def test_parser():
    parsed_element = quote.parser()
    parsed_element.reject_useless_info("Salut GrandPy ! Est-ce que tu connais"
                                       " l'adresse d'OpenClassrooms ?")
    assert parsed_element.result == "d'OpenClassrooms ?"

def test_wiki_response():
    summary = quote.research()
    summary.search("paris")
    assert len(summary.page_py.split()) > 3

