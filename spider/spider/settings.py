# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
   'Accept-Language': 'en',
    "cookie":'SESSIONID=9Upu5683WHbkNqdcb6Nx9IBNFhpe8Rxc1FPNQXPlX4R; osd=UV8XC07V_4WURI5uU96NEmZyVlBD8tmsumGpSHrw2KO9aqtJdaMNNsFGj2FUTN2zWVAU9OmTw06uRwJ05Sa0xlA=; JOID=UFkXBk3U-YWZR49oU9OOE2ByW1NC9NmhuWCvSHfz2aW9Z6hIc6MANcBAj2xXTduzVFMV8umewE-oRw935CC0y1M=; _zap=578652b6-14f9-4fa7-96fd-b7f672d42b64; d_c0="AAAunzIlnA-PTq-lJ_uWyDmz4KAWwmCYiP4=|1560956771"; q_c1=2e97d0f84ee246f4959489eb63b148c6|1560956773000|1560956773000; _ga=GA1.2.612682570.1586803215; _gid=GA1.2.597110080.1588751263; tst=r; _xsrf=cdZYan2ZKOEguUfm6USMoxjWDQvTZFa3; l_n_c=1; l_cap_id="NGUyODdjNDE1OTE2NDRkN2I2MWNiZmUwZTI3OWE2NzE=|1588918037|26a48b61e56f04d80e65d0550b82011f4716d69f"; r_cap_id="OGRmNDdjZjUyMjQzNGI3NTg2OWFjMzA4OWZhYTFjOTY=|1588918037|b59947fdaa40f71ad666ada0e9fc450e3ddbfd41"; cap_id="Yzk0ZjBiN2JjODQ4NDYxNTg3YWVhNGM2OGFmOTY3YTQ=|1588918037|6b9a068052bc90294febeaaa7aeb9ea3d365d64f"; n_c=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1588910574,1588915889,1588917620,1588918076; capsion_ticket="2|1:0|10:1588919525|14:capsion_ticket|44:ODFkYzhiZjIzMWI0NDFiOTljZTE2NmNiNDJkNTRjMGQ=|de3e8b01ec98cbee019bccf59aeb030cb86bee964f206bca315f64543a4853cf"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588919669; _gat_gtag_UA_149949619_1=1; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1588919671|1588915889'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spider.middlewares.SpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider.middlewares.SpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spider.pipelines.SpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL= 'ERROR'
