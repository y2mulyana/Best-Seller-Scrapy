import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    # allowed_domains = ['x']
    # url = 'https://www.amazon.co.uk/best-sellers-books-Amazon/zgbs/books/15512178031/ref=zg_bs_pg_{}?_encoding=UTF8&pg={}'

    # def start_requests(self):
    #     for i in range(1, 3):
    #         yield scrapy.Request(self.url.format(i))
    def start_requests(self):
        urls = [
            'https://www.amazon.co.uk/best-sellers-books-Amazon/zgbs/books/15512178031/ref=zg_bs_pg_1?_encoding=UTF8&pg=1',
            'https://www.amazon.co.uk/best-sellers-books-Amazon/zgbs/books/15512178031/ref=zg_bs_pg_2?_encoding=UTF8&pg=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for buku in response.xpath("//div[@id='gridItemRoot']"):
            yield{
               'Order' : buku.xpath('div/div[1]/div/span/text()').get(),
               'Title' : buku.xpath('div/div[2]/div/a/span/div/text()').get(),
               'Author': buku.xpath('div/div[2]/div/div[1]/a/div/text() |div/div[2]/div/div[1]/span/div/text()').get(),
               'Stars': buku.xpath('div/div[2]/div/div[2]/div/a/i/span/text()').get(),
               'Vote' : buku.xpath('div/div[2]/div/div[2]/div/a/span/text()').get(),
               'Edition': buku.xpath('div/div[2]/div/div[3]/span/text() | div/div[2]/div/div[2]/span/text()').get(),
               'Price' : buku.xpath('div/div[2]/div/div[4]/a/span/span/span/text()| div/div[2]/div/div[3]/a/span/span/span/text()').get(),
               'Asin': str(buku.xpath('div/div[2]/div/a/@href').get()).split('/')[3],
               'Link' : buku.xpath('div/div[2]/div/a/@href').get(),

            }

