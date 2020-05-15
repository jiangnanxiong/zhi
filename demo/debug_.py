import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    resp = requests.get(url, headers=headers).text
    return resp


with open("img_href2.txt", "r") as f:  # 打开文件
    data = f.readlines()


def pic_link():
    try:
        for n, l in enumerate(data):
            if n > 26335:
                print(n)
                link = l.strip('\n')
                soup = BeautifulSoup(get_html(link), "lxml")
                all_s = soup.select(
                    'body > main > div > section.content-info.clearfix > article > div.content-info_img > a > img')

                for img in all_s:
                    result2txt = str(img['src'])
                    with open('./img_link.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                        file_handle.write(result2txt)  # 写入
                        file_handle.write('\n')
    except Exception as e:
        print(e)


# pic_link()

# q = queue.Queue()
# for url in data:
#     q.put(url.strip('\n'))
# start = time.time()
# def fetch_img_func(q):
#     while True:
#         try:
#             url = q.get_nowait()# 不阻塞的读取队列数据
#             i = q.qsize()
#         except Exception as e:
#             print (e)
#             break
#         # print ('Current Thread Name Runing %s ... ' % threading.currentThread().name)
#         print("当前还有%s个任务"% i)
#         res = requests.get(url, stream=True)
#         if res.status_code == 200:
#             save_img_path ='./imgs/%s.jpg'%i
#             # 保存下载的图片
#             with open(save_img_path, 'wb') as fs:
#                 for chunk in res.iter_content(1024):
#                     fs.write(chunk)
#
# num=10  #线程数
# threads =[]
# for i  in range(num):
#     t = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_%s"%i)
#     threads.append(t)
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
#
# print(time.time()-start)
