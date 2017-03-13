import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from appcrawl.items import AppItem
import datetime

class AppstoreSpider(CrawlSpider):
    name = 'appstore'
    allowed_domains = ['itunes.apple.com']
    start_urls = ['http://itunes.apple.com/us/genre/ios-books/id6018?mt=8',
              'http://itunes.apple.com/us/genre/ios-business/id6000?mt=8',
              'http://itunes.apple.com/us/genre/ios-catalogs/id6022?mt=8',
              'http://itunes.apple.com/us/genre/ios-education/id6017?mt=8',
              'http://itunes.apple.com/us/genre/ios-entertainment/id6016?mt=8',
              'http://itunes.apple.com/us/genre/ios-finance/id6015?mt=8',
              'http://itunes.apple.com/us/genre/ios-food-drink/id6023?mt=8',
              'http://itunes.apple.com/us/genre/ios-games/id6014?mt=8',
              'http://itunes.apple.com/us/genre/ios-health-fitness/id6013?mt=8',
              'http://itunes.apple.com/us/genre/ios-lifestyle/id6012?mt=8',
              'http://itunes.apple.com/us/genre/ios-medical/id6020?mt=8',
              'http://itunes.apple.com/us/genre/ios-music/id6011?mt=8',
              'http://itunes.apple.com/us/genre/ios-navigation/id6010?mt=8',
              'http://itunes.apple.com/us/genre/ios-news/id6009?mt=8',
              'http://itunes.apple.com/us/genre/ios-newsstand/id6021?mt=8',
              'http://itunes.apple.com/us/genre/ios-photo-video/id6008?mt=8',
              'http://itunes.apple.com/us/genre/ios-productivity/id6007?mt=8',
              'http://itunes.apple.com/us/genre/ios-reference/id6006?mt=8',
              'https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8',
              'http://itunes.apple.com/us/genre/ios-social-networking/id6005?mt=8',
              'http://itunes.apple.com/us/genre/ios-sports/id6004?mt=8',
              'https://itunes.apple.com/us/genre/ios-stickers/id6025?mt=8',
              'http://itunes.apple.com/us/genre/ios-travel/id6003?mt=8',
              'http://itunes.apple.com/us/genre/ios-utilities/id6002?mt=8',
              'http://itunes.apple.com/us/genre/ios-weather/id6001?mt=8'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for href in hxs.xpath('//div[contains(@class,"column")]/ul/li/a/@href'):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_app)

    def parse_app(self, response): #parse_app
        hxs = Selector(response)
        i = AppItem()
        i['name'] = hxs.xpath('//div/div/h1/text()').extract_first()
        i['url'] = response.url
        i['id'] = response.url.split('/')[-1].split('?')[0][2:]
        i['category'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[2]/a/span/text()').extract_first()
        try:
            i['description'] = " ".join(hxs.xpath('//div[@id="content"]/div/div[2]/div[1]/p/text()').extract()).encode('ascii','ignore').strip()
        except:
            i['description'] = None
        try:
            i['new_version_desc'] = " ".join(hxs.xpath('//div[@id="content"]/div/div[2]/div[3]/p/text()').extract()).encode('ascii','ignore').strip()
        except:
            i['new_version_desc'] = None
        i['update_date'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[3]/span[2]/text()').extract_first()
        i['publish_date'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[3]/span[2]/@content').extract_first()
        i['scrape_date'] = datetime.date.today().isoformat()
        i['price'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[1]/span/div/text()').extract_first()
        i['version'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[4]/span[2]/text()').extract_first()
        i['size'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[5]/text()').extract_first()
        i['seller'] = hxs.xpath('//div[@id="left-stack"]/div[1]/ul/li[7]/span[2]/span/text()').extract_first()
        try:
            i['is_InAppPurcased'] = int('In-App' in hxs.xpath('//div[@id="left-stack"]/div[3]/h4/text()').extract_first())
        except:
            i['is_InAppPurcased'] = 0
        try:
            lang_str = hxs.xpath('//*[@id="left-stack"]/div[1]/ul/li[6]/text()').extract_first().split(',')
            i['is_multilingual'] = int(len(lang_str) > 1)
        except:
            i['is_multilingual'] = 0
        try:
            platform_str = int(hxs.xpath('//*[@id="left-stack"]/div[1]/div[1]/span[2]/text()').extract_first())
            i['is_multiplatform'] = int('and' in platform_str)
        except:
            i['is_multiplatform'] = 0
        try:
            i['current_rating'] = float(hxs.xpath('//div[@id="left-stack"]/div[2]/div[2]/span[1]/text()').extract_first())
        except:
            i['current_rating'] = None
        try:
            num_crating_str = hxs.xpath('//div[@id="left-stack"]/div[2]/div[2]/span[2]/text()').extract_first()
            i['num_current_rating'] = int(num_crating_str.split(' ')[0])
        except:
            i['num_current_rating'] = None
        try:
            orating_str = hxs.xpath('//div[@id="left-stack"]/div[2]/div[4]/@aria-label').extract_first()
            orating, num_orating_str = orating_str.split(',')
            i['overall_rating'] = orating
            i['num_overall_rating'] = int(num_orating_str.split(' ')[1])
        except:
            i['overall_rating'] = None
            i['num_overall_rating'] = None
        try:
            review1_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[1]/p/text()').extract_first()
            i['review1'] = review1_str.encode('ascii','ignore').strip()
            review1_stat_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[1]/h5/div/@aria-label').extract_first()
            i['review1_star'] = int(review1_stat_str.split(' ')[0])
        except:
            i['review1'] = None
            i['review1_star'] = None
        try:
            review2_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[2]/p/text()').extract_first()
            i['review2'] = review2_str.encode('ascii','ignore').strip()
            review2_stat_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[2]/h5/div/@aria-label').extract_first()
            i['review2_star'] = int(review2_stat_str.split(' ')[0])
        except:
            i['review2'] = None
            i['review2_star'] = None
        try:
            review3_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[3]/p/text()').extract_first()
            i['review3'] = review3_str.encode('ascii','ignore').strip()
            review3_stat_str = hxs.xpath('//div[@id="content"]/div/div[2]/div[5]/div[3]/h5/div/@aria-label').extract_first()
            i['review3_star'] = int(review3_stat_str.split(' ')[0])
        except:
            i['review3'] = None
            i['review3_star'] = None
        yield i

