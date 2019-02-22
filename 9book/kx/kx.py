# http://www.ecsponline.com/search.php?keywords=1&page=515
# http://www.ecsponline.com/search.php?page=1
# 132.232.210.52
# ubuntu
# pip install --user datetime
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
import  datetime
import  chardet
ua = UserAgent()
import sys
from lxml import etree

class KX_producs(object):
    def __init__(self,page=327):
        self.start=page
        self.url_key = 'http://www.ecsponline.com/search.php?keywords='
        self.url_page = 'http://www.ecsponline.com/search.php?page='
        self.speed = 0.5
        self.conn = pymysql.connect("localhost", "root", "admin", "book")
        self.cursor = self.conn.cursor()
        # self.ip_list=self.get_ip_list2()
        # self.ip_list=[{'ip': '125.33.71.198', 'port': 45731, 'expire_time': '2019-02-20 14:20:11', 'city': '北京市朝阳区'}, {'ip': '114.240.100.220', 'port': 4573, 'expire_time': '2019-02-20 14:11:52', 'city': '北京市朝阳区'}, {'ip': '111.196.135.242', 'port': 45731, 'expire_time': '2019-02-20 14:46:09', 'city': '北京市朝阳区'}, {'ip': '125.33.52.214', 'port': 45731, 'expire_time': '2019-02-20 14:21:32', 'city': '北京市朝阳区'}, {'ip': '124.64.245.132', 'port': 45731, 'expire_time': '2019-02-20 14:18:43', 'city': '北京市朝阳区'}, {'ip': '125.33.58.148', 'port': 4573, 'expire_time': '2019-02-20 14:09:45', 'city': '北京市朝阳区'}, {'ip': '111.196.130.74', 'port': 4573, 'expire_time': '2019-02-20 14:19:17', 'city': '北京市朝阳区'}, {'ip': '125.33.55.72', 'port': 4573, 'expire_time': '2019-02-20 14:58:25', 'city': '北京市朝阳区'}, {'ip': '123.119.46.29', 'port': 45731, 'expire_time': '2019-02-20 14:12:33', 'city': '北京市朝阳区'}, {'ip': '111.193.139.213', 'port': 4573, 'expire_time': '2019-02-20 18:22:12', 'city': '北京市朝阳区'}]
        # self.ip_list=[{'ip': '106.60.24.142', 'port': 4528, 'expire_time': '2019-02-20 13:58:24'}, {'ip': '182.37.77.243', 'port': 4572, 'expire_time': '2019-02-20 13:56:26'}, {'ip': '110.189.223.217', 'port': 4516, 'expire_time': '2019-02-20 21:10:39'}, {'ip': '114.217.109.190', 'port': 4536, 'expire_time': '2019-02-20 13:55:50'}, {'ip': '114.236.32.52', 'port': 45761, 'expire_time': '2019-02-20 13:53:06'}, {'ip': '113.76.139.203', 'port': 4523, 'expire_time': '2019-02-20 19:27:55'}, {'ip': '114.230.150.143', 'port': 4565, 'expire_time': '2019-02-20 17:50:18'}, {'ip': '115.224.211.49', 'port': 45671, 'expire_time': '2019-02-20 15:11:37'}, {'ip': '182.87.183.33', 'port': 45361, 'expire_time': '2019-02-20 14:30:27'}, {'ip': '182.44.197.89', 'port': 45721, 'expire_time': '2019-02-20 15:45:07'}]
        # self.ip_list =[{'ip': '117.67.141.140', 'port': 45951, 'expire_time': '2019-02-20 11:34:36'}, {'ip': '222.191.170.61', 'port': 45631, 'expire_time': '2019-02-20 11:12:01'}, {'ip': '114.234.225.199', 'port': 4543, 'expire_time': '2019-02-20 11:21:36'}, {'ip': '114.226.135.107', 'port': 45071, 'expire_time': '2019-02-20 11:28:16'}, {'ip': '115.239.21.189', 'port': 4531, 'expire_time': '2019-02-21 01:26:29'}, {'ip': '117.30.208.77', 'port': 45861, 'expire_time': '2019-02-20 11:29:25'}, {'ip': '117.31.144.55', 'port': 45351, 'expire_time': '2019-02-20 11:27:14'}, {'ip': '112.113.154.160', 'port': 45561, 'expire_time': '2019-02-20 15:27:38'}, {'ip': '116.149.195.81', 'port': 45361, 'expire_time': '2019-02-20 14:33:07'}, {'ip': '117.67.58.31', 'port': 45271, 'expire_time': '2019-02-20 11:22:09'}, {'ip': '119.118.145.220', 'port': 45291, 'expire_time': '2019-02-20 12:08:33'}, {'ip': '119.115.247.181', 'port': 45161, 'expire_time': '2019-02-20 11:19:14'}, {'ip': '60.169.94.165', 'port': 4547, 'expire_time': '2019-02-21 03:02:38'}, {'ip': '123.149.163.209', 'port': 45761, 'expire_time': '2019-02-20 15:53:46'}, {'ip': '220.189.86.133', 'port': 45311, 'expire_time': '2019-02-20 11:21:20'}, {'ip': '182.244.164.6', 'port': 4552, 'expire_time': '2019-02-20 14:16:48'}, {'ip': '36.57.76.244', 'port': 4548, 'expire_time': '2019-02-20 11:14:57'}, {'ip': '182.109.212.56', 'port': 45151, 'expire_time': '2019-02-20 11:10:24'}, {'ip': '112.114.88.22', 'port': 4571, 'expire_time': '2019-02-20 12:08:45'}, {'ip': '117.68.145.74', 'port': 4595, 'expire_time': '2019-02-20 11:17:33'}, {'ip': '175.153.20.45', 'port': 45461, 'expire_time': '2019-02-20 11:21:54'}, {'ip': '124.112.215.229', 'port': 4586, 'expire_time': '2019-02-20 11:26:17'}, {'ip': '101.27.23.149', 'port': 4562, 'expire_time': '2019-02-20 11:34:27'}, {'ip': '182.109.212.148', 'port': 45151, 'expire_time': '2019-02-20 11:27:56'}, {'ip': '117.57.34.231', 'port': 45731, 'expire_time': '2019-02-20 14:57:59'}, {'ip': '182.34.194.171', 'port': 4576, 'expire_time': '2019-02-20 11:16:32'}, {'ip': '106.57.6.114', 'port': 4528, 'expire_time': '2019-02-20 11:38:49'}, {'ip': '183.154.220.108', 'port': 4524, 'expire_time': '2019-02-20 11:20:22'}, {'ip': '60.169.115.225', 'port': 45471, 'expire_time': '2019-02-20 11:09:57'}, {'ip': '223.215.174.178', 'port': 45721, 'expire_time': '2019-02-20 11:07:06'}, {'ip': '183.149.184.39', 'port': 4547, 'expire_time': '2019-02-20 11:27:02'}, {'ip': '114.239.126.15', 'port': 45361, 'expire_time': '2019-02-20 12:57:09'}, {'ip': '220.176.92.153', 'port': 4518, 'expire_time': '2019-02-20 11:13:13'}, {'ip': '117.31.52.40', 'port': 45161, 'expire_time': '2019-02-20 12:12:18'}, {'ip': '112.252.69.168', 'port': 4537, 'expire_time': '2019-02-20 12:14:44'}]
        # self.storename = storename
        # self.headers = {
        #     "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 "
        #                  "(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
        # }
        # self.headers=  {"User-Agent": ua.random}
        # datenum = datetime.now().strftime('%Y%m%d%H%M')
        # self.filename = '{}_{}.csv'.format(self.storename, datenum)
        # self.get_file()
        # self.cookies= self.getcookies();

    def get_ip_list2(self,url='http://d.jghttp.golangapi.com/getip?num=10&type=2&pro=110000&city=110105&yys=0&port=11&pack=4848&ts=1&ys=0&cs=1&lb=1&sb=0&pb=45&mr=1&regions='):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        web_data = requests.get(url, headers=headers).text
        web_data = json.loads(web_data)
        ip_list = web_data["data"]
        print(ip_list)
        return ip_list
    def get_random_ip(self):
        ip_list = self.ip_list
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
    def open_html(self, fname):
        with open('.\\temp\\' + fname + ".html", 'rb') as htmlf:
            html = htmlf.read()
            html = str(html, 'utf-8')
            return html

    def save_html(self, url, fname="tm"):
        print(url)
        if (os.path.isfile(".\\temp\\" + fname + ".html")):
            # html = self.open_html(fname)
            # re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
            # error = "".join(re_error.findall(html))

            # if (error.__len__() and error in '您查看的页面找不到了!-理想生活上天猫' or html.__len__() == 0):
            #     time.sleep(3 * self.speed)
            # elif ("rgv587_flag" in html):
            #     infos = re.findall('({.*})', html)[0]
            #     infos = json.loads(infos)
            #     print(fname + "_error_" + "rgv587_flag")
            #     print(infos.get('url'))
            #     time.sleep(3 * self.speed)
            # else:
            #     print(" False")
            #     return False
            print(" False")
            return False

        t = 1
        s = self.speed
        while True:
            # headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
            # proxies={"https":"https://203.119.213.251:443"}
            headers = {"User-Agent": ua.random}
            # proxies = self.get_random_ip()
            # print(proxies)
            html = requests.get(url, headers=headers).content
            # html = requests.get(url, headers=headers ).content
            html_doc = str(html, 'utf-8')
            # re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
            # error = "".join(re_error.findall(html_doc))
            # if ((error.__len__() and error in '您查看的页面找不到了!-理想生活上天猫') or html.__len__() == 0):
            #     print("请求错误:" + error)
            #     time.sleep((60 * s * t))
            #     t = t * 2
            #     s = s + 1
            #     pass
            # elif ("rgv587_flag" in html_doc):
            #     # html_doc=html_doc.strip()
            #     html_doc = html_doc.replace("\r", "").replace("\n", "")
            #     infos = re.findall('({.*})', html_doc)
            #     infos = infos[0]
            #     infos = json.loads(infos)
            #     print(fname + "_error_" + "rgv587_flag")
            #     print(infos.get('url'))
            #     time.sleep(3 * self.speed)
            # else:
            if(1):
                with open(".\\temp\\" + fname + ".html", 'wb') as htmlf:
                    htmlf.write(html)
                    # nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # print(" Ture",nowtime)
                    # print(fname, html)
                    # time.sleep(self.speed * 1.0)
                    return True

    def db_close(self):
        if (self.conn):
            if (type(self.cursor) == 'object'):
                self.cursor.close()
            if (type(self.conn) == 'object'):
                self.conn.close()

    def db_insert(self, table_name, info_dict):
        """
        根据table_name与info自动生成建表语句和insert插入语句
        :param table_name: 数据需要写入的表名tm
        :param info_dict: 需要写入的内容，类型为字典
        :return:
        """
        sql_key = ''  # 数据库行字段
        sql_value = ''  # 数据库值
        sql_select = "select * from %s where 1=1 and %s = '%s'" % (table_name,list(info_dict.keys())[0],list((info_dict.values()))[0].replace("'","''"))
        print(sql_select)
        cursor = self.cursor
        conn = self.conn

        cursor.execute(sql_select)
        # 获取所有记录列表
        results = cursor.fetchall()
        if (results.__len__()):
            sql_update = ""
            for key in info_dict.keys():  # 生成insert插入语句
                sql_update = sql_update + "%s = '%s'," % (key, str(info_dict[key]))
            sql_update = "UPDATE %s set %s WHERE %s = '%s'" % (table_name,sql_update[:-1], list(info_dict.keys())[0],list((info_dict.values()))[0])
            print(sql_update)
            try:
                cursor.execute(sql_update)
                conn.commit()  # 提交当前事务

            except pymysql.Error as e:
                print("error update")
            self.db_close()
            return False

        for key in info_dict.keys():  # 生成insert插入语句
            sql_value = sql_value + "'" + str(info_dict[key]).replace("'","''") + "'" + ','
            sql_key = sql_key + ' ' + key + ','
        print("INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
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
    def main(self):
        total_page=1713
        time_temp=datetime.datetime(2019,2,2,11,11,11)
        for i in range(self.start,total_page+1):
            page = str(i)
            url = self.url_page + page
            fname = "kx_page_" + page
            flag=self.save_html(url, fname)

            nowtime = datetime.datetime.now()
            now=time.strftime("%Y-%m-%d %H:%M:%S")
            pre_time=(nowtime-time_temp)*(total_page-i)
            time_temp=nowtime
            print(flag,now,pre_time)
    def deal_data(self):
        for page in range(1185,1713+1):
            fname = "kx_page_" + str(page)
            html = self.open_html(fname)
            re_br = re.compile('\r\n')  # 处理换行
            re_br1 = re.compile(' ')  # 处理空格
            html = re_br.sub('', html)  # 去回车
            html = re_br1.sub('', html)  # 去空格
            # h=html.replace("\r\n", "").replace(" ", "")
            re_bname = re.compile(r'class="f6">(.*?)<br/></a>', re.S | re.M)
            re_bno = re.compile(r'书号：(.*?)', re.S | re.M)
            re_bauo = re.compile(r'作者：(.*?)', re.S | re.M)
            re_bset = re.compile(r'丛书名：(.*?)', re.S | re.M)
            re_botime = re.compile(r'出版日期：(.*?)', re.S | re.M)
            re_bhave = re.compile(r'库存：(.*?)', re.S | re.M)
            re_bcont = re.compile(r"<tr><tdcolspan='2'>内容简介：(.*?)</td></tr>", re.S | re.M)
            re_bprice = re.compile(r'style="padding-right:10px;">￥(.*?)元</font>', re.S | re.M)
            re_goodlist = re.compile(r'<ulclass="clearfixbgcolor"id=".*?">(.*?)</ul>', re.S | re.M)
            goodlist = re_goodlist.findall(html)
            re_td = re.compile(r'<td>(.*?)</td>', re.S | re.M)
            for good in goodlist:
                binfo = {}
                bifna = ["bname","bno" , "bauo", "bset", "botime", "bhave", "bprice", "bcont"]
                bin = []
                td = re_td.findall(good)
                bin.append(re_bname.findall(good)[0])
                bin.append(td[5].replace('书号：', ''))
                bin.append(td[6].replace('作者：', ''))
                bin.append(td[7].replace('丛书名：', ''))
                bin.append(td[9].replace('出版日期：', ''))
                bin.append(td[11].replace('库存：', ''))
                bin.append(re_bprice.findall(td[13])[0])
                bin.append(re_bcont.findall(good)[0])

                # bname = re_bname.findall(good)[0]
                # bno = td[5].replace('书号：', '')
                # bauo = td[6].replace('作者：', '')
                # bset = td[7].replace('丛书名：', '')
                # botime = td[9].replace('出版日期：', '')
                # bhave = td[11].replace('库存：', '')
                # bprice = re_bprice.findall(td[13])[0]
                for i in range(0, 8):
                    binfo[bifna[i]] = bin[i]
                flag = self.db_insert("kx", binfo)
                print(flag, bin[0], bin[1])
            print(str(page)+"完成")

if __name__ == '__main__':
    storename = 'kxcbs'
    if (len(sys.argv) > 1):
        page=int(sys.argv[1])
    else:
        page=1185
    # print("page:"+str(page))
    kx = KX_producs(page)
    # kx.main()
    kx.deal_data()



