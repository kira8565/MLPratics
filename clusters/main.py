import feedparser
import re


def getWordCount(url):
    d = feedparser.parse(url)


getWordCount("http://news.qq.com/newsgn/rss_newsgn.xml")
