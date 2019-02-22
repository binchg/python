import request
from lxml import etree
import requests
import json
import base64
import bs4
import re
import time
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import os
import pymysql
import datetime
import simplejson as json
import random
from fake_useragent import UserAgent
import requests
import json
import csv
import random
import re
from datetime import datetime
import time
from fake_useragent import UserAgent
import  chardet
ua = UserAgent()
import  chardet
ua = UserAgent()
startpage=1
# pagenum=getpagenum()
pagenum=200
speed =3
conn = pymysql.connect("localhost","root","admin","weibo" )
cursor = conn.cursor()
def db_insert(table_name, info_dict):
    """
    根据table_name与info自动生成建表语句和insert插入语句
    :param table_name: 数据需要写入的表名
    :param info_dict: 需要写入的内容，类型为字典
    :return:
    """
    sql_key = ''  # 数据库行字段
    sql_value = ''  # 数据库值
    sql_select="select * from wb_essay where 1=1 and we_id = '%s'"% info_dict["we_id"]
    # print(info_dict["we_id"],sql_select)
    cursor.execute(sql_select)
    # 获取所有记录列表
    results = cursor.fetchall()
    if(results.__len__()):
        sql_update =""
        for key in info_dict.keys():# 生成insert插入语句
            sql_update=sql_update + "%s = '%s',"%(key,info_dict[key])
        sql_update = "UPDATE wb_essay set %s WHERE we_id = '%s'"%(sql_update[:-1],info_dict["we_id"])
        # print(sql_update)
        try:
            cursor.execute(sql_update)
            conn.commit()  # 提交当前事务
        except pymysql.Error as e:
            print("error update")
        return False


    for key in info_dict.keys():  # 生成insert插入语句
        sql_value = sql_value + "'" + info_dict[key] + "'" + ','
        sql_key = sql_key + ' ' + key + ','
    # print("INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
    try:
        cursor.execute( "INSERT INTO %s (%s) VALUES (%s)" % (table_name, sql_key[:-1], sql_value[:-1]))
        conn.commit()  # 提交当前事务
    except pymysql.Error as e:
        if str(e).split(',')[0].split('(')[1] == "1146":  # 当表不存在时，生成建表语句并建表
            sql_key_str = ''  # 用于数据库创建语句
            columnStyle = ' text'  # 数据库字段类型
            for key in info_dict.keys():
                sql_key_str = sql_key_str + ' ' + key + columnStyle + ','
            cursor.execute("CREATE TABLE %s (%s)" % (table_name, sql_key_str[:-1]))
            cursor.execute("INSERT INTO %s (%s) VALUES (%s)" %(table_name, sql_key[:-1], sql_value[:-1]))
            conn.commit()  # 提交当前事务
        else:
            raise
    return True
def getcookies():
    # cookie = "SUB=_2A25xL1x1DeRhGeVM61MV8SzKyT2IHXVS0GQ9rDV6PUJbkdANLXDskW1NTTyy53nZ2TPvyntFuvbawDD7fkMZmD6u; SUHB=0G0uqTq5nzeXJa; SCF=AuSAj3Rq-61GTDQWEYCsAEfeeqMB__QtrOgm_5o1PYYeT5HyalUcrRRhGCOjn9McVrmjE1Rvg5Oi0Jwyt5XYnr0.; _T_WM=fcb1ab8a7a5026ef89241ed66f551e70; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=09e7b1; M_WEIBOCN_PARAMS=oid%3D4339627114072875%26luicode%3D20000061%26lfid%3D4339627114072875%26uicode%3D20000061%26fid%3D4339627114072875"
    cookie = "cna=AkmNFBy1qjICAd9o/wR+Nydb; x=__ll%3D-1%26_ato%3D0; _m_h5_tk=328f05c33325641d7c93beec1c747acf_1550488622679; _m_h5_tk_enc=99e35e6435d7dd6e67d7bf0225294470; lid=kinggold98; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=URm48syIYn73&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTZ5OXpG5R4Gg%3D%3D&tag=10&lng=zh_CN; uc3=vt3=F8dByEzfiaGjdj%2F4Ycg%3D&id2=UU2y8J%2Bq3U7uEg%3D%3D&nk2=CN5OZl35a2T%2Bfw%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; tracknick=kinggold98; _l_g_=Ug%3D%3D; ck1=""; unb=2507913654; lgc=kinggold98; cookie1=BvAGdW%2BLwb%2FkOyzbqBK8X70M%2FRmP99B%2B7JucAfqmEBE%3D; login=true; cookie17=UU2y8J%2Bq3U7uEg%3D%3D; cookie2=1b8c51ed609a78fa60eea5ad79b4042e; _nk_=kinggold98; t=a254038476abcbf561e55afe5eed0861; uss=""; csg=133c3056; skt=a0bcbd3bcf29e738; _tb_token_=e803bf77ee35; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=BMjIoFqfAIAoOGwFVRe4fZ8omTbacSx7-yNi14J5F8M2XWjHKoBSC1oU0XWI3uRT; l=bBTYULRnvH3LBbGGBOCanurza779jIRxjuPzaNbMi_5d9681RvbOllYQkFJ6Vj5R_M8B41UUP5v9-etlv"
    cookies = {}
    for s in cookie.split('; '):
        t = s.split('=')
        cookies[t[0]] = t[1]
    return cookies
def save_html(url,fname="weibo"):
    if(os.path.isfile(".\\temp\\"+fname+".html")):
        html=open_html(fname)
        re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
        error="".join(re_error.findall(html))
        if(error.__len__() and error in '微博-出错了 502 Bad Gatewa 登录 - 新浪微博'):
            time.sleep(3*speed)
        else:
            return False
    t = 1
    s = speed
    while True:
        headers = {"User-Agent": ua.random}
        r=requests.get(url, cookies=getcookies(), headers=headers)
        html = r.content
        html_doc = str(html, 'utf-8')
        re_error = re.compile(r'<title>(.*?)</title>', re.I | re.S | re.M)
        error = "".join(re_error.findall(html_doc))

        if (error.__len__() and error in '微博-出错了 502 Bad Gatewa 登录 - 新浪微博'):
            print("请求错误:"+error)
            time.sleep((60*s*t))
            t = t *2
            s=s+1
        else:
            with open(".\\temp\\" + fname + ".html", 'wb') as htmlf:
                htmlf.write(html)
                # print(fname, html)
                time.sleep(speed)
                return html
    # filehandle = open(".\\temp\\"+fname+".html", 'wb')#wb以格式覆盖写入
    # html = html.decode(chardet['encoding']).encode('utf-8')

# 读取本地网页为str
def open_html(fname):
    with open('.\\temp\\'+fname+".html", 'r', encoding="utf-8") as htmlf:
        html = htmlf.read()
        # print(html)
        return html

def get_products(self,page):
        '''提取单页商品列表'''
        num = random.randint(83739921, 87739530)
        endurl = '/shop/shop_auction_search.do?sort=s&p={}&page_size=12&from=h5&ajson=1&_tm_source=tmallsearch&callback=jsonp_{}'
        url = self.url + endurl.format(page,num)
        html = requests.get(url, cookies=self.cookies,headers=self.headers).text
        infos = re.findall('\(({.*})\)', html)[0]
        infos = json.loads(infos)
        products = infos.get('items')
        # 商品id，价格，评价，月销售量，标题，总销售，详情链接，图片链接
        title = ['item_id', 'price', 'quantity', 'sold', 'title', 'totalSoldQuantity', 'url', 'img']
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=title)
            writer.writerows(products)
save_html("https://kxcbs.m.tmall.com/shop/shop_auction_search.do?spm=a1z60.7754813.0.0.301755f0pZ1GjU&sort=defaul&p=1","kxcbs1")