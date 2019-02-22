# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random
import urllib.request
import json
import time

def get_ip_list(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text, 'html')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    #检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
          proxy_host = "https://" + ip
          print(proxy_host)
          proxy_temp = {"https": proxy_host}
          res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
          ip_list.remove(ip)
          continue
    print(ip_list)
    return ip_list
def getHTMLText(url,proxies):
    try:
        r = requests.get(url,proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return 0
    else:
        return r.text
def get_ip_list2(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web_data = requests.get(url, headers=headers).text
    web_data = json.loads(web_data)
    ip_list=web_data["data"]
    print(ip_list)
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip_data in ip_list:
        nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ip_time=ip_data["expire_time"]
        if(nowtime>ip_time):
            continue
        ip=ip_data["ip"]+":"+str(ip_data["port"])
        ip_proxy='https://' + ip
        print(ip,ip_proxy)
        proxy_list.append(ip_proxy)
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


if __name__ == '__main__':
    url = 'http://d.jghttp.golangapi.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&pack=4848&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
    ip_list = get_ip_list2(url)
    # ip_list =[{'ip': '27.209.251.32', 'port': 4537, 'expire_time': '2019-02-19 19:33:51'}, {'ip': '114.228.249.17', 'port': 45761, 'expire_time': '2019-02-19 19:55:56'}, {'ip': '182.107.173.40', 'port': 45631, 'expire_time': '2019-02-19 19:34:15'}, {'ip': '59.60.239.130', 'port': 45161, 'expire_time': '2019-02-19 20:48:31'}, {'ip': '122.195.216.49', 'port': 45071, 'expire_time': '2019-02-20 04:21:21'}, {'ip': '123.189.130.117', 'port': 4568, 'expire_time': '2019-02-19 22:41:12'}, {'ip': '49.79.36.66', 'port': 4506, 'expire_time': '2019-02-20 00:45:11'}, {'ip': '182.244.165.149', 'port': 4528, 'expire_time': '2019-02-19 19:44:28'}, {'ip': '117.95.198.56', 'port': 45361, 'expire_time': '2019-02-19 19:40:04'}, {'ip': '36.56.150.225', 'port': 4516, 'expire_time': '2019-02-19 19:36:39'}]
    proxies = get_random_ip(ip_list)
    print(proxies)
    


# ['221.235.235.85:9999', '171.41.80.99:9999', '222.135.92.68:38094', '116.209.53.121:9999', '111.177.171.217:9999', '171.41.82.155:9999', '183.148.139.44:9999', '111.177.187.22:9999', '125.123.136.106:9000', '111.177.189.218:9999', '115.151.0.73:9999', '111.177.187.219:9999', '116.209.58.47:9999', '121.61.3.95:9999', '125.123.139.195:9999', '116.209.59.74:9999', '222.94.148.114:3128', '113.128.30.38:9999', '112.87.64.32:9999', '111.177.178.167:9999', '125.123.136.43:9999', '123.163.121.122:9999', '111.177.178.45:9999', '111.177.171.30:9999', '183.148.132.66:9999', '218.91.112.220:9999', '111.177.172.3:9999', '112.85.165.211:9999', '111.177.162.255:9999', '112.85.164.100:9999', '112.85.171.182:9999', '111.177.177.254:9999', '222.128.9.235:59593', '123.233.215.211:8118', '144.123.70.206:9999', '125.123.143.4:9999', '113.128.30.201:39008', '121.61.1.194:9999', '113.128.8.181:23945', '111.181.62.192:9999', '116.209.59.236:9999', '180.119.68.96:9999', '111.177.179.129:9999', '144.255.14.185:21096', '111.177.175.128:9999', '180.119.141.38:808', '116.62.215.123:8118', '111.177.175.202:9999', '121.61.0.91:9999', '111.177.170.10:9999']
