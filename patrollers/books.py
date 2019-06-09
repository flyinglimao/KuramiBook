from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq

class BooksPatroller(PatrollerInterface):
    def __init__(self):
        super(BooksPatroller, self).__init__("https://activity.books.com.tw/books66/", "博客來")

    def generate(self):
        dom = pq(url=self.url)
        # 取得當日
        day = dom("#cntdwn").text()
        today = pq(url="https://activity.books.com.tw/crosscat/ajaxinfo/getBooks66OfTheDayAjax/P?uniqueID=" + dom("#cntdwn + div").attr("id"))
        link = today("a").attr("href")
        image = today("img").attr("src")
        name = today("h1").text()
        price = today(".price b:nth-child(2)").text()
        book = Book(name, link, image, price)
        self.dataset.set_book(day, book)
        # 取得接下來 6 日
        for discount in dom(".date").parent():
            discount = pq(discount)
            day = discount(".date").text()
            link = discount("a").attr("href")
            image = discount("img").attr("src")
            name = discount("img").attr("alt")
            price = discount(".price b").text()
            book = Book(name, link, image, price)
            self.dataset.set_book(day, book)
        return self.dataset