class Article:
    def __init__(self, text, coords, id):
        self.text = text
        self.coords = coords
        self.id = id

    def __lt__(self, other):
        return len(self.text) < len(other.text)