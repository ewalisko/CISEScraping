# Scrapy settings for ISATScraping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CISEScraping'

SPIDER_MODULES = ['CISEScraping.spiders']
NEWSPIDER_MODULE = 'CISEScraping.spiders'
ITEM_PIPELINES = {'CISEScraping.pipelines.saveToFile':500}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CISEScraping (+http://www.yourdomain.com)'
