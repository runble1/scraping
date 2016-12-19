import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.yahoo.co.jp"]
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        """
        トップページのトピックス一覧からここのトピックスへのリンクを抜き出して表示する
        """
        print(response.css('ul.topics a::attr("href")').extract())
