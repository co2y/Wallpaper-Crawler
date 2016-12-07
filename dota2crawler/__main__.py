# coding=utf-8
from __future__ import print_function, unicode_literals
from bs4 import BeautifulSoup
from utils.utils import print_error, print_success, unicodeize
from dota2crawler.config import BASE_URL, DOTA2_URL
from dota2crawler.config import IS_PYTHON3
import requests
import signal
import sys
import os

# python2 or python3
if IS_PYTHON3:
    _unicode = str
else:
    _unicode = unicode


# global Ctrl-C signal handler
def signal_handler(signal, frame):
    print_error('User aborted, quit')


signal.signal(signal.SIGINT, signal_handler)

# save directory
save_dir = os.path.abspath('./pic') if len(sys.argv) < 2 \
    else os.path.abspath(sys.argv[1])

if os.path.exists(save_dir):
    if not os.path.isdir(save_dir):
        print_error('pic exists as a file, specify directory')
else:
    os.mkdir(save_dir)


# request url
def get_response(url):
    try:
        return unicodeize(requests.get(url).content)
    except requests.ConnectionError:
        print_error('error: failed to establish a new connection')


# get all pages and image url
def get_info(url):
    response = get_response(url)
    if not response:
        print_error('error: failed to request url')
    else:
        soup = BeautifulSoup(response, 'lxml')
        pagenum = int(soup.select('.page_select')[-1].string)
    get_one(soup)


# first page image url
def get_one(soup):
    divtags = soup.find_all(class_='preview_size')
    downlist = []
    for divtag in divtags:
        downlist.append(divtag.h3.a['href'])
    download(downlist)


# save wallpaper to local
def download(downlist):
    for url in downlist:
        filename = url.split('/')[-2]
        resolution = url.split('/')[-1]
        imageurl = BASE_URL + 'image/' + filename + '_' + resolution + '.jpg'
        ir = requests.get(imageurl)
        if ir.status_code == 200:
            open(os.path.join(save_dir, filename + '.jpg'),
                 'wb').write(ir.content)
            print_success(filename + ' download successful')
        else:
            print_error(filename + ' download failed')


# other page image url
def get_all():
    pass


# run
get_info(DOTA2_URL)
