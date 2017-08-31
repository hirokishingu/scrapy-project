from scrapy.spiders import SitemapSpider

class WiredjpSpider(SitemapSpider):
    name = "wiredjp"
    allowed_domains = ["wired.jp"]

    sitemap_urls = ["http://wired.jp/robots.txt",]

    sitemap_follow = [r"post-2015-",]

    sitemap_rules = [(r'/2015/\d\d/\d\d/', 'parse_post'),]

    def parse_post(self, response):
        yield {
            "title" : response.css("h1.post-title::text").extract_first(),
        }