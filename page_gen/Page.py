

class Page:

    def __init__(self, text, name, path):
        self.text = text
        self.name = name
        self.path = path
        self.html_path = "%s.html" % self.path

    def factory(text, name):
        return Page(text, name)
