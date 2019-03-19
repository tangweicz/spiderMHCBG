#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#! -*-coding:utf-8-*-

import requests,subprocess,time,os,datetime

#
# headStr = {
#
#             'Accept': '*/*',
#
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
#
#             'Accept-Encoding': 'gzip, deflate, sdch',
#
#             'Accept-Language': 'zh-CN,zh;q=0.8'
# }
#
# try:
#
#     res = requests.get("https://recommd.xyq.cbg.163.com/cgi-bin/recommend.py?callback=Request.JSONP.request_map.request_0&_=1539830579182&level_min=109&level_max=109&expt_gongji=17&expt_fangyu=17&expt_fashu=17&expt_kangfa=17&bb_expt_gongji=17&bb_expt_fangyu=17&bb_expt_fashu=17&bb_expt_kangfa=17&act=recommd_by_role&page=1&count=15&search_type=overall_search_role&view_loc=overall_search", proxies={"http": "http://1.10.186.48:59102"}, headers=headStr, timeout=3, allow_redirects=False)
#
#     print(res.text)
#
#
#
# except:
#
#     pass
#
#
# exit()






while True:

    print(datetime.datetime.now())

    os.chdir("/Users/tangwei/pythonProject/mhcbg/mhcbg")

    subprocess.run("/Library/Frameworks/Python.framework/Versions/3.6/bin/scrapy crawl cbg163", shell=True)

    print("stop crawl")

    print(datetime.datetime.now())

    time.sleep(60*60)



# import requests,json
#
# headStr = {
#
#             'Accept': '*/*',
#
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
#
#             'Accept-Encoding': 'gzip, deflate, sdch',
#
#             'Accept-Language': 'zh-CN,zh;q=0.8',
#
#             'Referer':'http://wzw.zhong5.cn/index.php?g=Wap&m=Zvoteimg&a=index&token=xfwqiv1454723052&id=152&code=071SoMJg1NySOy0LoTHg1x0MJg1SoMJF&state=',
#
#             'Cookie':"lTUZ_eb82_smile=7D1; __utma=82552285.325934957.1505023649.1515770785.1531871164.3; __utmz=82552285.1531871164.3.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); pgv_pvi=9841789020; lTUZ_eb82_ulastactivity=3cffrR1sN0c6rDFlRxq7w6dyUb7RISgY93UsqLc%2BsuxoWRdaBVKG; lTUZ_eb82_lastcheckfeed=733258%7C1534665245; lTUZ_eb82_connect_is_bind=0; PHPSESSID=t2oqv4daq6aau7o974i3onuhj6; oauth2_xfwqiv1454723052=%7B%22wap_token%22%3A%22xfwqiv1454723052%22%2C%22wecha_id%22%3A%22owuiVuKhJw5b6RiY_ZBO7DJcQDjs%22%2C%22appid%22%3A%22wx806ca43dfa9f5d77%22%7D; __guid=11247858.1971322277786610200.1542711549553.09; monitor_count=1; alert_state_0=1"
#
#         }
#
# res = requests.get("http://wzw.zhong5.cn/index.php?g=Wap&m=Zvoteimg&a=vote&vote_id=152&token=xfwqiv1454723052&id=66705", headers=headStr)
#
# print(json.loads(res.content.decode("gbk")))