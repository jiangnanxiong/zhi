import requests
from bs4 import BeautifulSoup
import os
import re


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    resp = requests.get(url, headers=headers).text
    return resp


def all_page():
    base_url = 'https://www.tnc.com.cn/search/products-c-90-k--p{}.html'
    urllist = []
    for page in range(1, 201):
        allurl = base_url.format(page)
        urllist.append(allurl)
    return urllist


def htmp_prase():
    for url in all_page():
        soup = BeautifulSoup(get_html(url), "xml")
        alltitle = soup.find('ul', class_='blog-item-contain')
        title_tmp = alltitle.find_all('a')
        title = []
        for k in title_tmp:
            title.append(k.string)
        alllink = alltitle.find_all('img')
        link = []
        for k in alllink:
            link.append(k['src'])
        counter = 0
        for k in link:
            if k[0:5] != 'http://www.hansight.com':
                k = 'http://www.hansight.com' + k
                link[counter] = k
            counter += 1
        mkdir(title)
        download(title, link)


def htmp_prase2():
    url_links = set()
    for url in all_page():
        soup = BeautifulSoup(get_html(url), "lxml")
        all_s = soup.find_all(class_='clicktrack img')
        n = 0
        for url_link in all_s:
            url_links.add(url_link['href'])
            n += 1
            print(n)

        print(url_links)
        print(len(url_links))
        # print(all_s)
        # getTags(alltitle)
        # title = []
        # for k in title_tmp:
        #     title.append(k.string)
        # alllink = alltitle.find_all('img')
        # link = []
        # for k in alllink:
        #     link.append(k['src'])
        # counter = 0
        # for k in link:
        #     if k[0:5] != 'http://www.hansight.com':
        #         k = 'http://www.hansight.com' + k
        #         link[counter] = k
        #     counter += 1
        # mkdir(title)
        # download(title, link)


# htmp_prase2()


# uri = 'https://www.tnc.com.cn/product/d155485.html'
#
# soup = BeautifulSoup(get_html(uri), "lxml")
# all_s = soup.find_all(class_='clearfix')
# print(all_s)


# s=set()
# for a in all_s:
#     s.add(a['href'])


def mkdir(title):
    for name in title:
        path = "I://python//爬虫//"
        os.mkdir(path + name)
        os.chdir(path + name)
        path_ = "I://python//爬虫//" + name + '.jpg'
        os.chdir("I://python//爬虫//")


def download(title, link):
    counter = 0
    for url in link:
        name = title[counter]
        file = requests.get(url).content
        path = "I://python//爬虫//" + name + '//' + name + '.jpg'
        f = open(path, 'wb')
        f.write(file)
        f.close()
        counter += 1

# htmp_prase()
# print('文件已保存')
