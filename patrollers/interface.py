class Dataset:
    def __init__(self):
        self.data = {}

    def set_book(self, day, book):
        day = day.strip()
        self.data[day] = book
    
    def __jsonencode__(self):
        return self.data

class Book:
    def __init__(self, name, link, image, price):
        self.name = name
        self.link = link
        self.image = image
        self.price = int(price)
    
    def __jsonencode__(self):
        return {
            "name": self.name,
            "link": self.link,
            "image": self.image,
            "price": self.price
        }

class PatrollerInterface(object):
    def __init__(self, url="", name=""):
        self.url = url
        self.name = name
        self.dataset = Dataset()

    def generate(self):
        pass