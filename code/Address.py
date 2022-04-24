# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import requests
import DDConf

class DDAddress:

    def __init__(self,vaildAdd):
        self.Id = vaildAdd['id']
        self.Name = vaildAdd['location']['name']
        self.StationId = vaildAdd['station_id']
        self.CityNumber = vaildAdd["city_number"]
        self.Longitude = vaildAdd["location"]["location"][0]
        self.Latitude = vaildAdd["location"]["location"][1]
        self.UserName = vaildAdd["user_name"]
        self.Mobile = vaildAdd["mobile"]
        self.Address = vaildAdd["location"]["address"]
        self.AddrDetail = vaildAdd["addr_detail"]

    def __str__(self):
        return 'DDAddress (id：%s, name：%s,stationId：%s,CityNumber：%s,Longitude：%s,' \
               'Latitude：%s,UserName：%s, Mobile：%s,Address：%s,AddrDetail：%s)' \
               % (self.Id, self.Name,self.StationId,self.CityNumber,self.Longitude,
                  self.Latitude,self.UserName,self.Mobile,self.Address,self.AddrDetail)

def getAddress():
    cookies = {
        'DDXQSESSID': DDConf.DDXQSESSID,
    }

    headers = {
        'Host': 'sunquan.api.ddxq.mobi',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN',
        'referer': 'https://servicewechat.com/wx1e113254eda17715/422/page-frame.html',
    }

    params = (
        ('city_number', '0101'),
        ('api_version', '9.49.2'),
        ('app_version', '2.82.0'),
        ('applet_source', ''),
        ('channel', 'applet'),
        ('app_client_id', '4'),
        ('sharer_uid', ''),
        ('s_id', ''),
        ('openid', ''),
        ('h5_source', ''),
        ('source_type', '5'),
    )

    response = requests.get('https://sunquan.api.ddxq.mobi/api/v1/user/location/', headers=headers, params=params, cookies=cookies)
    addresList = []
    print(response.json())
    if(response.status_code == 200):
        vaildAddres = response.json()['data']['my_addresses']
        for addr in vaildAddres:
            addresList.append(DDAddress(addr))
    return addresList

if __name__ == '__main__':
    print(getAddress())