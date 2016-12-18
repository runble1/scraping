import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider' # Spiderの名前
    # クロールを開始するURLリスト
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        """
        トップページからカテゴリページへのリンクを抜き出してたどる
        """
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.REquest(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        """
        カテゴリページからそのカテゴリの投稿のタイトルを全て抜き出す
        """
        for post_title in response.css('div.entries > ul > li a::text').extract():
             yield {'title': post_title}
