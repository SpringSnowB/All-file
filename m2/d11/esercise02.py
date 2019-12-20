"""
编写一个函数，传入端口名称，返回这个端口所描述的信息中，
对应的address值

注意：段与段之间有空行
每段首单词是端口名
"""
import re

def find_address(port):
    f = open('./exc')
    data = f.read().split('\n\n')
    for par in data:
        if  re.search(r'\S+',par).group() == port:
            return re.search(r'(\d+\.){3}\d/\d+|Unknown+',par).group()
    return '未找到该地址'

if __name__ == '__main__':
    result = find_address('Loopback0')
    print(result)


