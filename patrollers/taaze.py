from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq

class TaazePatroller(PatrollerInterface):
    def __init__(self):
        super(TaazePatroller, self).__init__("https://www.taaze.tw/act66.html", "讀冊生活")

    def generate(self):
        dom = pq(url=self.url)
        discount_root = dom("[src=\"/include/act/img/week-66.jpg\"]").closest("table")
        discounts = discount_root("tr:nth-child(n+1) table table")
        for discount in discounts:
            discount = pq(discount)
            day = discount(".date").text().replace("\n", "")
            link = discount("td:nth-child(2) a").attr("href")
            image = discount("td:nth-child(2) img").attr("src")
            name = discount(".txt-b").text()
            price = discount("td:nth-child(3) tr:nth-child(3) span:nth-child(2)").text()
            if day != None and name != None and link != None and image != None and price != None:
                book = Book(name, link, image, price)
                self.dataset.set_book(day, book)
        return self.dataset