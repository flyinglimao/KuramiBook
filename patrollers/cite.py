from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq

class CitePatroller(PatrollerInterface):
    def __init__(self):
        super(CitePatroller, self).__init__("https://www.cite.com.tw/76a4e", "城邦讀書花園")

    def generate(self):
        dom = pq(url=self.url, encoding="big5")
        # 取得當日
        today = pq(dom(".sale-now .pdset-1:nth-child(1)"))
        day = today(".box-title").text()[:9]
        link = "https://www.cite.com.tw/" + today(".photo a").attr("href")
        image = "https:" + today(".photo img").attr("src")
        name = today(".photo img").attr("title")
        price = today(".book > p").text()[-4:-1]
        book = Book(name, link, image, price)
        self.dataset.set_book(day, book)
        # 取得接下來 6 天
        discounts_root = pq(dom(".book-list")[0])
        for discount in discounts_root(".item"):
            discount = pq(discount)
            day = discount(".date").text()
            link = "https://www.cite.com.tw/" + discount(".photo a").attr("href")
            image = "https:" + discount(".photo img").attr("src")
            name = discount(".photo img").attr("title")
            price = discount(".price").text()[-4:-1]
            book = Book(name, link, image, price)
            self.dataset.set_book(day, book)
        return self.dataset