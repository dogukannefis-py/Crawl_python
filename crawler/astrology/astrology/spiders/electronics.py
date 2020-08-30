# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.olx.com.pk']
    start_urls = [
        'http://www.olx.com.pk/computers-accessories/',
        'http://www.olx.com.pk/tv-video-audio/',
        'https://www.olx.com.pk/games-entertainment/']

    rules=(Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),  ##pageNextPrev is the class that will be used to fetch the links to next pages.
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..'+response.url)
        item_links = response.css('.large > .detailsLink::attr(href)').extract()
                for a in item_links:
                    yield scrapy.Request(a, callback=self.parse_detail_page)
