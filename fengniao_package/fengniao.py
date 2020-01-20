#-*- coding: utf-8 -*-
#--------------------------------------------------
#@Time: 2020/1/17 15:44
#@Author: Administrator
#@IDE: PyCharm
# Description: 
#--------------------------------------------------

import os
import requests
from bs4 import BeautifulSoup
import time
from python_package3 import summation
from fengniao_package.python_package1 import divsion
from fengniao_package.python_package2 import mul
import lxml


class downloader(object):
    def __init__(self):
        self.server = 'http://image.fengniao.com/'
        # url = 'http://www.fengniao.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.a_hrefs = []
        self.img_srcs = []

    #获取请求
    def get_response(self,url):
        data = requests.get(url,headers=self.headers).content.decode('gbk')
        return data

    #解析列表数据数据
    def url_list(self,data):
        #转类型
        soup = BeautifulSoup(data,'lxml')
        #解析内容
        url_list = soup.select(".pic75")
        print(url_list)
        # return url_list
        urls = []
        for url in url_list:
            url = url.get('href')
            urls.append(url)
        return urls

    #解析目标页数据
    def detali_data(self,url):
        data = requests.get(url,headers = self.headers).content
        soup = BeautifulSoup(data,'lxml')

        src_list = soup.select('img')
        srcs =[]
        for src in src_list:
            src = src.get('src')
            srcs.append(src)
        return srcs

    #判断文件是否存在
    # def check_file(self):

    #打开并存储目标页数据链接的内容
    def save_picture(self,url):

        filepath =url.spilt(159)[1]
        data = requests.get(url,headers=self.headers).content
        dir = './fengniao/'
        if not os.path.exists(dir):
            os.makedirs(dir)
        out_file = dir + filepath + '.jpg'

        with open(out_file,'wb')as f:
            f.write(data)

    #保存数据
    def save_data(self,data):
        with open('fengniao.html','w')as f:
            f.write(data)


if __name__ == '__main__':
    # print(summation.sum(2, 3))
    # print(divsion.chu(9,3))
    # print(mul.mul(2,3))
    d = downloader()
    #获取数据
    data = d.get_response(d.server)
    #解析得到列表数据
    urls = d.url_list(data)
    #保存数据
    d.save_data(data)
    #解析得到图片列表
    n = 1
    for url in urls:
        srcs = d.detali_data(url)
        print('--------------------------')
        print(n)
        n += 1
        for src in srcs:
            time.sleep(1)
            print(src)
            # d.save_picture(src)
