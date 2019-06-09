from .interface import PatrollerInterface, Book
from pyquery import PyQuery as pq
from datetime import datetime

class KingStonePatroller(PatrollerInterface):
    def __init__(self):
        super(KingStonePatroller, self).__init__("https://www.kingstone.com.tw/event/0708_aonsale66/predict66.asp", "金石堂")

    def generate(self):
        dom = pq("https://www.kingstone.com.tw/new", headers={"user-agent": "pyquery"})
        day = datetime.now().strftime("%m/%d(%w)")
        day = day[:6] + ['日', '一', '二', '三', '四', '五', '六'][int(day[6])] + day[7:]
        link = "https://www.kingstone.com.tw" + dom(".saleindexunit a").attr("href")
        image = dom(".saleindexunit img").attr("src")
        name = dom(".saleindexunit img").attr("alt")
        price = dom(".saleindexunit .priceset span:nth-child(2) b")[0].text
        book = Book(name, link, image, price)
        self.dataset.set_book(day, book)

        dom = pq(url=self.url, headers={"user-agent": "pyquery"}) # 金石堂需要 User-Agent Header，否則會 400
        for discount in dom(".datecolumn")[:6]:
            discount = pq(discount)
            day = discount(".date_predict66").text()
            link = "https://www.kingstone.com.tw" + discount(".mainbox2 a").attr("href")
            image = discount(".mainbox2 img").attr("data-original")
            name = discount(".mainbox2 h3").text()
            price = discount(".mainbox2 .sale_price:nth-child(3)").text()
            book = Book(name, link, image, price)
            self.dataset.set_book(day, book)
        return self.dataset