import requests
from bs4 import BeautifulSoup
import os
import re


def all_page():
    base_url = 'https://sc.macw.com/atlas/16483_{}.html'
    urllist = []
    for page in range(1, 6):
        allurl = base_url.format(page)
        urllist.append(allurl)
        # print(allurl)
    return urllist


# url='https://sc.macw.com/atlas/16483_1.html'
#
# soup = BeautifulSoup(get_html(url), "lxml")
# all_s = soup.select('body > main > div > section.material-list > ul > li > a')
# for link in all_s:
#     print(link['href'])


def htmp_prase2():
    url_links = set()
    for url in all_page():
        soup = BeautifulSoup(get_html(url), "lxml")
        all_s = soup.select('body > main > div > section.material-list > ul > li > a')
        for link in all_s:
            print(link['href'])
            url_links.add(link['href'])
        print(len(url_links))
        print(url_links)



def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    resp = requests.get(url, headers=headers).text
    return resp


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def download_img(img_url, index):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    r = requests.get(img_url, headers=headers, stream=True, timeout=10)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('D:\\PY_DEMO_1\\imgs/{}.jpg'.format(index), 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


def down(uri, num):
    try:
        soup = BeautifulSoup(get_html(uri), "lxml")
        all_s = soup.select(
            'body > main > div > section.content-info.clearfix > article > div.content-info_img > a > img')
        imgs = []
        for img in all_s:
            imgs.append(img['src'])
        for i in imgs:
            download_img(i, num)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    with open("img_href.txt", "r") as f:
        data = f.readlines()
    for num, link in enumerate(data):
        if num >=23576:
            link = link.strip('\n')
            print('第{}条链接'.format(num + 1))
            down(link, num)

