class Article:
    def __init__(self, text, coords, id, type='ro_cp'):
        self.text = text
        self.coords = coords
        self.id = id
        self.type = type


    def __lt__(self, other):
        return len(self.text) < len(other.text)