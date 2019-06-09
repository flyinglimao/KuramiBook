from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq

class IReadPatroller(PatrollerInterface):
    def __init__(self):
        super(IReadPatroller, self).__init__("https://www.iread.com.tw/alldiscount.aspx", "灰熊愛讀書")

    def generate(self):
        dom = pq(url=self.url)
        discounts = dom(".BOX2")
        for discount in discounts:
            discount = pq(discount)
            raw_day = discount(".Date").text()
            day = raw_day[:2] + "/" + raw_day[3:5] + "(" + raw_day[-1] + ")"
            link = "https://www.iread.com.tw/" + discount(".BookCover a").attr("href")
            image = "https://www.iread.com.tw/" + discount(".BookCover img").attr("src")
            name = discount(".BookTitle").text()
            price = discount(".Price .redword:nth-child(2)").text()
            if day != None and name != None and link != None and image != None and price != None:
                book = Book(name, link, image, price)
                self.dataset.set_book(day, book)
        return self.dataset