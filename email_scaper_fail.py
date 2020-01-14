#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:38:56 2019

@author: kyleschneider
"""

"""import pandas as pd
import requests as r
from bs4 import BeautifulSoup

URL = 'https://webapps.akc.org/breeder-referral/#/'

headers = {"User_Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = r.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

"""
"""print(soup.prettify())"""


"""myp = soup.findAll("p", {"class": "increaseBottomMargin ng-scope"})

print(myp)"""


from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
 
# a queue of urls to be crawled
new_urls = deque(['https://www.crossfit.com/'])
 
# a set of urls that we have already crawled
processed_urls = set()
 
# a set of crawled emails
emails = set()
 
# process urls one by one until we exhaust the queue
while len(new_urls):
 
    # move next url from the queue to the set of processed urls
    url = new_urls.popleft()
    processed_urls.add(url)
 
    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
 
    # get url's content
    print("Processing %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors
        continue
 
    # extract all email addresses and add them into the resulting set
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
 
    # create a beutiful soup for the html document
    soup = BeautifulSoup(response.text)
 
    # find and process all the anchors in the document
    for anchor in soup.find_all("a"):
        # extract link url from the anchor
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        # add the new url to the queue if it was not enqueued nor processed yet
        if not link in new_urls and not link in processed_urls:
            new_urls.append(link)