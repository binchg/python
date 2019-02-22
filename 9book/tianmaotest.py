# -*- coding: utf-8 -*-
import requests
import json
import csv
import random
import re
from datetime import datetime
import time
from fake_useragent import UserAgent
import os
import pymysql
from bs4 import BeautifulSoup
import requests
import random
import urllib.request
import json
import time
import  chardet
ua = UserAgent()

class TM_producs(object):

    def __init__(self,storename):
        self.start=77
        self.storename = storename
        self.url = 'https://{}.m.tmall.com'.format(storename)
        # self.headers = {
        #     "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 "
        #                  "(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
        # }
        # self.headers=  {"User-Agent": ua.random}

        datenum = datetime.now().strftime('%Y%m%d%H%M')
        self.filename = '{}_{}.csv'.format(self.storename, datenum)
        # self.get_file()
        self.cookies= self.getcookies();
        self.speed = 3
        self.conn = pymysql.connect("localhost", "root", "admin", "book")
        self.cursor = self.conn.cursor()
        self.ip_list=self.get_ip_list2()
        # self.ip_list =[{'ip': '221.227.231.172', 'port': 45361, 'expire_time': '2019-02-19 19:57:19'},
        #  {'ip': '220.189.87.104', 'port': 45311, 'expire_time': '2019-02-19 21:27:31'},
        #  {'ip': '171.125.161.167', 'port': 4587, 'expire_time': '2019-02-19 19:51:09'},
        #  {'ip': '175.153.21.244', 'port': 4546, 'expire_time': '2019-02-19 20:00:18'},
        #  {'ip': '58.243.15.98', 'port': 4586, 'expire_time': '2019-02-19 20:13:31'},
        #  {'ip': '222.220.111.97', 'port': 4578, 'expire_time': '2019-02-19 20:28:42'},
        #  {'ip': '114.238.167.126', 'port': 45601, 'expire_time': '2019-02-19 20:02:38'},
        #  {'ip': '180.109.34.110', 'port': 4566, 'expire_time': '2019-02-19 19:54:25'},
        #  {'ip': '121.226.45.50', 'port': 4536, 'expire_time': '2019-02-20 00:05:13'},
        #  {'ip': '144.123.70.40', 'port': 4537, 'expire_time': '2019-02-19 19:58:37'}]
    def getcookies(self):
        # cookie = "SUB=_2A25xL1x1DeRhGeVM61MV8SzKyT2IHXVS0GQ9rDV6PUJbkdANLXDskW1NTTyy53nZ2TPvyntFuvbawDD7fkMZmD6u; SUHB=0G0uqTq5nzeXJa; SCF=AuSAj3Rq-61GTDQWEYCsAEfeeqMB__QtrOgm_5o1PYYeT5HyalUcrRRhGCOjn9McVrmjE1Rvg5Oi0Jwyt5XYnr0.; _T_WM=fcb1ab8a7a5026ef89241ed66f551e70; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=09e7b1; M_WEIBOCN_PARAMS=oid%3D4339627114072875%26luicode%3D20000061%26lfid%3D4339627114072875%26uicode%3D20000061%26fid%3D4339627114072875"
        cookie="enc=31O1FU9NvFBqiPwWIPmse0yBdKmZ%2FTbTFKQb0%2B%2Br0AnubmhKbpH5aRO2aZLkut9TfiXXZoeWWre2vropcwaqjg%3D%3D; sm4=500106; _m_h5_tk=b94ecf209492518650858a1b99939583_1550585869803; _m_h5_tk_enc=9a1c423efdcc24c082f4e25cd8781e14; cna=/igYFHlnw1wCAXuT9jIX1sdN; isg=BLu7SNJVY66fkljgDlIL0sELRJ_luORTZdSZYa14JrrxDNvuNeHhYtmFIuznNycK; l=bBafBeplvPBfAph5BOfaNuIRXRQ9wIR34kPzw4ZCgICP9uf68rLfWZZL_5YBC3GVw14HR3JjcDO9BeYBqXC..; hng=CN%7Czh-CN%7CCNY%7C156; t=a7f182f74f50583758666b59f6351d31; uc3=vt3=F8dByEzfip11wCdMstA%3D&id2=UU2y8J%2Bq3U7uEg%3D%3D&nk2=CN5OZl35a2T%2Bfw%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=kinggold98; lid=kinggold98; lgc=kinggold98; _tb_token_=53337b97fee7; cookie2=1a250f3b90ee164be2908941c3942772"
        cookies = {}
        for s in cookie.split('; '):
            t = s.split('=')
            cookies[t[0]] = t[1]
        return cookies

    # def get_random_ip(ip_list):
    #     proxy_list = []
    #     for ip in ip_list:
    #         proxy_list.append('http://' + ip)
    #     proxy_ip = random.choice(proxy_list)
    #     proxies = {'http': proxy_ip}
    #     return proxies
    def get_ip_list2(self,url = 'http://d.jghttp.golangapi.com/getip?num=50&type=2&pro=&city=0&yys=0&port=11&pack=4848&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        web_data = requests.get(url, headers=headers).text
        web_data = json.loads(web_data)
        ip_list = web_data["data"]
        print(ip_list)
        return ip_list
    def get_random_ip(self):
        ip_list=self.ip_list
        proxy_list = []
        for ip_data in ip_list:
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            ip_time = ip_data["expire_time"]
            if (nowtime > ip_time):
                continue
            ip = ip_data["ip"] + ":" + str(ip_data["port"])
            ip_proxy = 'https://' + ip
            # print(ip_proxy,ip_time)
            proxy_list.append(ip_proxy)
        proxy_ip = random.choice(proxy_list)
        proxies = {'https': proxy_ip}
        return proxies
    # def get_proxies(self):
    #     ip_list=[
    #         '115.213.152.145:4508',
    #         '114.104.143.23:4548',
    #         '180.119.193.139:4565',
    #         '222.135.92.68:38094'
    #     ]
    #     proxy_list = []
    #     for ip in ip_list:
    #         proxy_list.append('https://' + ip)
    #     proxy_ip = random.choice(proxy_list)
    #     print(proxy_ip)
    #     proxy_temp = {'https': proxy_ip}
    #     return proxy_temp
    def open_html(self,fname):
        with open('.\\temp\\' + fname + ".html", 'rb') as htmlf:
            html = htmlf.read()
            html = str(html, 'utf-8')
            return html

    def save_html(self,url, fname="tm"):
        print(url)
        if (os.path.isfile(".\\temp\\" + fname + ".html")):
            html = self.open_html(fname)
            re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
            error = "".join(re_error.findall(html))

            if (error.__len__() and error in '您查看的页面找不到了!-理想生活上天猫' or html.__len__()==0 ):
                time.sleep(3 * self.speed)
            elif("rgv587_flag"in html):
                infos = re.findall('({.*})', html)[0]
                infos = json.loads(infos)
                print(fname+"_error_"+"rgv587_flag")
                print(infos.get('url'))
                time.sleep(3 * self.speed)
            else:
                print(" False")
                return False
        t = 1
        s = self.speed
        while True:
            headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
            # proxies={"https":"https://203.119.213.251:443"}
            # headers = {"User-Agent": ua.random}
            proxies = self.get_random_ip()
            html = requests.get(url, cookies=self.cookies, headers=headers).content
            html_doc = str(html, 'utf-8')
            re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
            error = "".join(re_error.findall(html_doc))
            if ((error.__len__() and error in '您查看的页面找不到了!-理想生活上天猫')or html.__len__()==0):
                print("请求错误:" + error)
                time.sleep((60 * s * t))
                t = t * 2
                s = s + 1
                pass
            elif ("rgv587_flag" in html_doc):
                # html_doc=html_doc.strip()
                html_doc=html_doc.replace("\r", "").replace("\n", "")
                infos = re.findall('({.*})', html_doc)
                infos=infos[0]
                infos = json.loads(infos)
                print(fname + "_error_" + "rgv587_flag")
                print(infos.get('url'))
                time.sleep(3 * self.speed)
            else:
                with open(".\\temp\\" + fname + ".html", 'wb') as htmlf:
                    htmlf.write(html)
                    print(" Ture")
                    # print(fname, html)
                    time.sleep(self.speed*5)
                    return html
        # filehandle = open(".\\temp\\"+fname+".html", 'wb')#wb以格式覆盖写入
        # html = html.decode(chardet['encoding']).encode('utf-8')

    # 读取本地网页为str
    def db_close(self):
        if (self.conn):
            if (type(self.cursor) == 'object'):
                self.cursor.close()
            if (type(self.conn) == 'object'):
                self.conn.close()
    def db_insert(self,table_name, info_dict):
        """
        根据table_name与info自动生成建表语句和insert插入语句
        :param table_name: 数据需要写入的表名tm
        :param info_dict: 需要写入的内容，类型为字典
        :return:
        """
        sql_key = ''  # 数据库行字段
        sql_value = ''  # 数据库值
        sql_select = "select * from tm where 1=1 and item_id = '%s'" % str(info_dict["item_id"])
        # print(info_dict["item_id"],sql_select)
        cursor=self.cursor
        conn=self.conn

        cursor.execute(sql_select)
        # 获取所有记录列表
        results = cursor.fetchall()
        if (results.__len__()):
            sql_update = ""
            for key in info_dict.keys():  # 生成insert插入语句
                sql_update = sql_update + "%s = '%s'," % (key, str(info_dict[key]))
            sql_update = "UPDATE tm set %s WHERE item_id = '%s'" % (sql_update[:-1], info_dict["item_id"])
            print(sql_update)
            try:
                cursor.execute(sql_update)
                conn.commit()  # 提交当前事务

            except pymysql.Error as e:
                print("error update")
            self.db_close()
            return False

        for key in info_dict.keys():  # 生成insert插入语句
            sql_value = sql_value + "'" + str(info_dict[key]) + "'" + ','
            sql_key = sql_key + ' ' + key + ','
        # print("INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
        try:
            cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
            conn.commit()  # 提交当前事务
        except pymysql.Error as e:
            if str(e).split(',')[0].split('(')[1] == "1146":  # 当表不存在时，生成建表语句并建表
                sql_key_str = ''  # 用于数据库创建语句
                columnStyle = ' text'  # 数据库字段类型
                for key in info_dict.keys():
                    sql_key_str = sql_key_str + ' ' + key + columnStyle + ','
                cursor.execute("CREATE TABLE %s (%s)" % (table_name, sql_key_str[:-1]))
                cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
                conn.commit()  # 提交当前事务
            else:
                raise
        self.db_close()
        return True
    def get_file(self):
        '''创建一个含有标题的表格'''
        title = ['item_id','price','quantity','sold','title','totalSoldQuantity','url','img']
        with open(self.filename,'w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=title)
            writer.writeheader()
        return

    def getpagenum(self):
        url = self.url
        endurl = '/search.htm?pageNo=1&viewType=list'
        url = self.url + endurl
        self.save_html(url, self.storename)
        html = self.open_html(self.storename)
        # 获取微博页数，每页10个
        res_pagenum = r'<b class="ui-page-s-len">1/(.*?)</b>'  # 处理页数
        pagenum = re.findall(res_pagenum, html, re.I | re.S | re.M)
        print(int(pagenum[0]))
        return int(pagenum[0])
    def get_totalpage(self):
        '''提取总页码数'''
        # num = random.randint(83739921,87739530)
        endurl = '/shop/shop_auction_search.do?sort=defaul&p=1'
        # url = self.url + endurl.format(num)
        url = self.url + endurl
        self.save_html(url, self.storename)
        html=self.open_html(self.storename)
        infos = re.findall('({.*})',html)
        infos=infos[0]
        infos = json.loads(infos)
        totalpage = infos.get('total_page')
        return int(totalpage)

    def get_products(self,page):
        '''提取单页商品列表'''
        num = random.randint(83739921, 87739530)
        endurl = '/shop/shop_auction_search.do?sort=defaul&p={}'
        url = self.url + endurl.format(page)
        fname=self.storename+"page_" + str(page)
        self.save_html(url,fname )
        html=self.open_html(fname)
        # html = requests.get(url, cookies=self.cookies,headers=self.headers).text
        infos = re.findall('({.*})', html)[0]
        infos = json.loads(infos)
        products = infos.get('items')
        # 商品id，价格，评价，月销售量，标题，总销售，详情链接，图片链接
        title = ['item_id', 'price', 'quantity', 'sold', 'title', 'totalSoldQuantity', 'url', 'img']
        for data in products:
            print(data, self.db_insert("tm", data))
        # with open(self.filename, 'a', newline='') as f:
        #     writer = csv.DictWriter(f, fieldnames=title)
        #     writer.writerows(products)
    def get_product_html(self):
        page=1
        url="https://kxcbs.tmall.com/search.htm?pageNo={}"
        url.format(page)
        fname="tm_{}"
        fname.format(page)
        self.save_html(url,fname)
    def main(self):
        '''循环爬取所有页面宝贝'''
        # total_page = self.get_totalpage()
        total_page = 891
        # self.get_random_ip()
        for i in range(self.start,total_page+1):
            self.get_products(i)
            print('总计{}页商品，已经提取第{}页'.format(total_page,i))
            time.sleep(self.speed)
        # self.get_totalpage()
if __name__ == '__main__':
    storename = 'kxcbs'
    tm = TM_producs(storename)
    tm.main()