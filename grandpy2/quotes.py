import wikipedia


class research:

    def __init__(self):
        self.page_py = ""
        self.articles = []

    def search(self, desired_location):
        wikipedia.set_lang("fr")

        try:
            self.page_py = wikipedia.page(desired_location)
        except wikipedia.exceptions.DisambiguationError as e:
            self.articles = e.options

    def disamb(self, desired_location):
        wikipedia.set_lang("en")
        try:
            self.articles = wikipedia.search(desired_location)
        except wikipedia.exceptions.DisambiguationError as e:
            self.articles = e.options

        self.html_list = self.articles

        # for a in self.articles:
        #    self.html_list.append(a)







