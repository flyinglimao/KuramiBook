from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq

class KingStonePatroller(PatrollerInterface):
    def __init__(self):
        super(KingStonePatroller, self).__init__("https://www.kingstone.com.tw/event/0708_aonsale66/predict66.asp", "金石堂")

    def generate(self):
        dom = pq(url=self.url, headers={"user-agent": "pyquery"}) # 金石堂需要 User-Agent Header，否則會 400
        for discount in dom(".datecolumn"):
            discount = pq(discount)
            day = discount(".date_predict66").text()
            link = "https://www.kingstone.com.tw/" + discount(".mainbox2 a").attr("href")
            image = discount(".mainbox2 img").attr("src")
            name = discount(".mainbox2 h3").text()
            price = discount(".mainbox2 .sale_price:nth-child(2)").text()
            book = Book(name, link, image, price)
            self.dataset.set_book(day, book)
        return self.dataset