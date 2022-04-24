# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import requests
import  DDConf

def checkCart():
    cookies = {
        'DDXQSESSID': DDConf.DDXQSESSID,
    }

    headers = {
        'Host': 'maicai.api.ddxq.mobi',
        'content-type': 'application/x-www-form-urlencoded',
        'ddmc-city-number': DDConf.DDAdder.CityNumber,
        'ddmc-build-version': '2.82.0',
        'ddmc-station-id': DDConf.DDAdder.StationId,
        'accept':'application/json, text/plain, */*',
        'ddmc-channel': 'undefined',
        'ddmc-uid': DDConf.UID,
        'ddmc-os-version': 'undefined',
        'ddmc-app-client-id': '4',
        'x-requested-with': "com.yaya.zone",
        'sec-fetch-site':'same-site',
        'ddmc-api-version': '9.49.2',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN',
        'referer': 'https://servicewechat.com/wx1e113254eda17715/422/page-frame.html',
    }

    params = (
        ('station_id', DDConf.DDAdder.StationId),
        ('city_number', DDConf.DDAdder.CityNumber),
        ('api_version', '9.49.2'),
        ('app_version', '2.82.0'),
        ('applet_source', ''),
        ('channel', 'applet'),
        ('app_client_id', '4'),
        ('sharer_uid', ''),
        ('s_id', ''),
        ('openid', ''),
        ('h5_source', ''),
        ('is_load', '1'),
        ('ab_config', '{"key_onion":"D","key_cart_discount_price":"C"}'),

    )
    for num in range(1, 100):
        response = requests.get('https://maicai.api.ddxq.mobi/cart/index', headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            if response.json()['code'] == 0:
                new_order_product_list = response.json()['data']['new_order_product_list']
                print(response.json())
                if len(new_order_product_list) == 0:
                    print('购物车货品为空')
                    continue
                else:
                    products = new_order_product_list[0]['products']
                    parent_order_sign = response.json()['data']['parent_order_info']['parent_order_sign']
                    return products,parent_order_sign
            else:
                print('购物车接口重试...')
                continue
    return [],''
if __name__ == '__main__':
    checkCart()