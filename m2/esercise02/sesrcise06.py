"""
利用给出的函数功能完成：
创建若干个进程或者线程，每个进程线程下载其中一章内容，要求同时下载执行。

爬虫
"""
import requests
from threading import Thread
# from multiprocessing import Process
# import signal
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 获取章节地址列表
def text():
    list_ = []
    response = requests.get('https://www.17k.com/list/3015690.html')
    html = response.text
    for line in html.split():
        if 'href' in line and 'chapter' in line :
            url = line.split('"')[-2]
            list_.append("www.17k.com"+url)
    return list_

# 传入一个章节地址，和第几章，返回该章节网页内容
def download(url,num):
    response = requests.get('https://'+url)
    txt_ = response.content
    # 存放的位置
    print("正在下载第%s章"%num)
    with open('./xs/第%d章.html'%num,mode='wb') as f:
        f.write(txt_)
count = 1
url_list = text()
def download_url():
    global count
    while True:
        if url_list:
            url = url_list.pop(0)
            download(url,count)
            count += 1
        else:
            return


jobs = []

def main():
    for i in range(10):
        t = Thread(target=download_url)
        t.start()
        jobs.append(t)

if __name__ == '__main__':
    main()
    [job.join() for job in jobs]


