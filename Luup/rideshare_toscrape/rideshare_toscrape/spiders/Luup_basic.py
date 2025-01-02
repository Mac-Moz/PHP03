import scrapy
import re

class LuupBasicSpider(scrapy.Spider):
    name = 'Luup_basic'
    allowed_domains = ['luup.sc'] #ドメイン名のみに変更['luup.sc/news/'] ['luup.sc']
    start_urls = ['https://luup.sc/news'] #URLの修正['http://luup.sc/news//'] ['https://luup.sc/news']

    def parse(self, response):
        articles = response.xpath('//div[contains(@class,"column")]/ul/li')
        


        for article in articles:
                    # タイトル、日付、画像、リンクを抽出
                    title = article.xpath('.//p[contains(@class,"content")]/text()').get()
                    date = article.xpath('.//time/@datetime').get()
                    image = article.xpath('.//img/@src').get()
                    link = article.xpath('./a/@href').get()

                    # データの整形（不要なホワイトスペースを削除）
                    title = re.sub(r'\s+', ' ', title.strip()) if title else None

                    # データを出力
                    yield {
                        'title': title,
                        'date': date,
                        'image': image,
                        'link': link
                    }
