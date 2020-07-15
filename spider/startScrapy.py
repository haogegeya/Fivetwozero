import os
from scrapy import cmdline
from config import logging

from multiprocessing import Process


def start():
    print(os.getcwd())
    logging.INFO("爬虫开始")
    resourceCwd = os.getcwd()
    os.chdir(os.path.join(resourceCwd,"spider"))
    cmdline.execute('scrapy crawl zhihu'.split())
    os.chdir(resourceCwd)
    print(os.getcwd())

def startOtherProcess():
    pro = Process(target=start)
    pro.start()
