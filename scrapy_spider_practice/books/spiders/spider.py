# -*- coding: utf-8 -*-
import scrapy

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    #xpath = //tagname[@Attribute="Value"]  
    #Reference: https://www.guru99.com/xpath-selenium.html
    def parse(self, response):
        #article is the book pane
        all_the_books = response.xpath('//article')
        print(len(all_the_books))
        
        #the book is the article, so omit article from xpath
        for book in all_the_books:
            #For whole HTML: response.xpath('// ...
            #For one loop element: response.xpath('.// ...  This searches in the element rather than all the HTML.
            title = book.xpath('.//h3/a/@title').extract_first()
            #Use scrapy shell 'URL' to experiment to get correct price
            price=book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('.//a/img/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
            yield {
                'Title': title,
                'Price': price,
                'Image_URL': image_url,
                'Book_URL': book_url
            }

#Save yielded result to file.  scrapy crawl spider -o books.csv
