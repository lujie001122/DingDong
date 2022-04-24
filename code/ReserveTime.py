# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import requests
import json
import DDConf

def GetMultiReserveTime():
    cookies = {
        'DDXQSESSID': DDConf.DDXQSESSID
    }

    headers = {
        'Host': 'maicai.api.ddxq.mobi',
        'ddmc-city-number': DDConf.DDAdder.CityNumber,
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN',
        'accept':"application/json, text/plain, */*",
        'ddmc-os-version': '[object Undefined]',
        'ddmc-channel': 'applet',
        'ddmc-build-version': '2.82.0',
        'content-type': 'application/x-www-form-urlencoded',
        'ddmc-app-client-id': '4',
        'ddmc-station-id': DDConf.DDAdder.StationId,
        'ddmc-uid': DDConf.UID,
         "origin": "https://wx.m.ddxq.mobi",
        'referer': 'https://servicewechat.com/wx1e113254eda17715/422/page-frame.html',
        'ddmc-ip': '',
        'x-requested-with': "com.yaya.zone",
        'sec-fetch-site': 'same-site',
        'ddmc-api-version': '9.49.2',
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    product = str(json.dumps(DDConf.Products))
    data = {
        'station_id': DDConf.DDAdder.StationId,
        'city_number': DDConf.DDAdder.CityNumber,
        'api_version': '9.49.2',
        'app_version': '2.82.0',
        'applet_source': '',
        'app_client_id': '4',
        'sharer_uid': '',
        'h5_source': '',
        's_id': '',
        'openid': '',
        'group_config_id': '',
        "products": '['+product+']',
        "isBridge": "false",
    }

    for num in range(1, 100):
        response = requests.post('https://maicai.api.ddxq.mobi/order/getMultiReserveTime', headers=headers, data=data,
                                 cookies=cookies)
        timeList = []
        if response.status_code == 200:
            if response.json()['code'] == 0:
                times = response.json()['data'][0]['time'][0]['times']
                for time in times:
                    if time['disableType'] == 0:
                        timeList.append(time)
        if(len(timeList) > 0):
            print(timeList)
            print("====")
            return timeList
        else:
            continue
if __name__ == '__main__':
    GetMultiReserveTime()