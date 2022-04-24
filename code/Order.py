# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import requests
import json
import DDConf


def checkOrder():
    cookies = {
        'DDXQSESSID': DDConf.DDXQSESSID,
    }

    headers = {
        'Host': 'maicai.api.ddxq.mobi',
        'content-type': 'application/x-www-form-urlencoded',
        'ddmc-city-number': DDConf.DDAdder.CityNumber,
        'ddmc-build-version': '2.82.0',
        "accept": "application/json, text/plain, */*",
        'ddmc-channel': 'applet',
        'ddmc-os-version': '[object Undefined]',
        'ddmc-app-client-id': '4',
        'ddmc-ip': '',
        'ddmc-uid': DDConf.UID,
        "ddmc-station-id":DDConf.DDAdder.StationId,
        'ddmc-api-version': '9.49.2',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN',
        'referer': 'https://servicewechat.com/wx1e113254eda17715/422/page-frame.html',
    }
    DDConf.TimesList[0]['start_timestamp']
    productList = []
    for product in DDConf.Products:

        tmp = {
            "id": product['id'],
            "total_money": product['total_price'],
            "total_origin_money": product['origin_price'],
            "count": product['count'],
            "price": product['price'],
            "instant_rebate_money": "0.00",
            "origin_price": product['origin_price'],
            "sizes": [],
        }
        productList.append(tmp)
    packagesInfo = {
        "package_type": 1,
        "package_id": 1,
        "products": productList,

        'reserved_time':{
            'reserved_time_start':DDConf.TimesList[0]['start_timestamp'],
            'reserved_time_end':DDConf.TimesList[0]['end_timestamp']
        }
    }
    packagesStr = str(json.dumps(packagesInfo))
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
        "user_ticket_id": "default",
        "freight_ticket_id": "default",
        "is_use_point": "0",
        "is_use_balance": "0",
        "is_buy_vip":"0",
        "coupons_id": "",
        "is_buy_coupons": "0",
        "packages": '['+packagesStr+']',
        "check_order_type": "0",
        "is_support_merge_payment": "1",
        "showData": "true",
        "showMsg": "false",
    }
    # data = 'uid=5e075ebb9a811b874798ccba&longitude=116.317071&latitude=39.841724&station_id=5f8d0c23bac21c0001186331&city_number=0201&api_version=9.49.2&app_version=2.82.0&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=da911b94655cf973cfe79b77589785e9&openid=osP8I0VJqGMKA98Rar2qUwnOdeVg&h5_source=&device_token=WHJMrwNw1k%2FF0qdLNvE01AV0nGtUhf%2FMbEskbKA0IJJsIgD0pc86qnBHo6vIROLgBIKOHz%2FfQD8hjI0rJceyDXyuDTF1rRBhndCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&address_id=624ecac9fdc0bc0001de6fd1&user_ticket_id=default&freight_ticket_id=default&is_use_point=0&is_use_balance=0&is_buy_vip=0&coupons_id=&is_buy_coupons=0&packages=%5B%7B%22products%22%3A%5B%7B%22id%22%3A%226109066dd991bad33cc44e3e%22%2C%22category_path%22%3A%22%22%2C%22count%22%3A1%2C%22price%22%3A%227.90%22%2C%22total_money%22%3A%227.90%22%2C%22instant_rebate_money%22%3A%220.00%22%2C%22activity_id%22%3A%22%22%2C%22conditions_num%22%3A%22%22%2C%22product_type%22%3A0%2C%22sizes%22%3A%5B%5D%2C%22type%22%3A1%2C%22total_origin_money%22%3A%227.90%22%2C%22price_type%22%3A0%2C%22batch_type%22%3A-1%2C%22sub_list%22%3A%5B%5D%2C%22order_sort%22%3A2%2C%22origin_price%22%3A%227.90%22%7D%2C%7B%22id%22%3A%2258b7df76936edf7a323cf16c%22%2C%22category_path%22%3A%2258f9e5a1936edf89778b568b%2C58fb3b9b936edfc0408b586c%22%2C%22count%22%3A1%2C%22price%22%3A%229.90%22%2C%22total_money%22%3A%229.90%22%2C%22instant_rebate_money%22%3A%220.00%22%2C%22activity_id%22%3A%22%22%2C%22conditions_num%22%3A%22%22%2C%22product_type%22%3A0%2C%22sizes%22%3A%5B%5D%2C%22type%22%3A1%2C%22total_origin_money%22%3A%229.90%22%2C%22price_type%22%3A0%2C%22batch_type%22%3A-1%2C%22sub_list%22%3A%5B%5D%2C%22order_sort%22%3A3%2C%22origin_price%22%3A%229.90%22%7D%5D%2C%22total_money%22%3A%2217.80%22%2C%22total_origin_money%22%3A%2217.80%22%2C%22goods_real_money%22%3A%2217.80%22%2C%22total_count%22%3A2%2C%22cart_count%22%3A2%2C%22is_presale%22%3A0%2C%22instant_rebate_money%22%3A%220.00%22%2C%22total_rebate_money%22%3A%220.00%22%2C%22used_balance_money%22%3A%220.00%22%2C%22can_used_balance_money%22%3A%220.00%22%2C%22used_point_num%22%3A0%2C%22used_point_money%22%3A%220.00%22%2C%22can_used_point_num%22%3A0%2C%22can_used_point_money%22%3A%220.00%22%2C%22is_share_station%22%3A0%2C%22only_today_products%22%3A%5B%5D%2C%22only_tomorrow_products%22%3A%5B%5D%2C%22package_type%22%3A1%2C%22package_id%22%3A1%2C%22front_package_text%22%3A%22%E5%8D%B3%E6%97%B6%E9%85%8D%E9%80%81%22%2C%22front_package_type%22%3A0%2C%22front_package_stock_color%22%3A%22%232FB157%22%2C%22front_package_bg_color%22%3A%22%23fbfefc%22%2C%22reserved_time%22%3A%7B%22reserved_time_start%22%3A1649415600%2C%22reserved_time_end%22%3A1649417400%7D%7D%5D&check_order_type=0&is_support_merge_payment=1&showData=true&showMsg=false&nars=69da5da50c25254751fa073a0f7442a4&sesi=5OlpxeD0a3c4cc6cb6f3f3f2453acce1ba55b18'
    for num in range(1, 200):
        response = requests.post('https://maicai.api.ddxq.mobi/order/checkOrder', headers=headers, cookies=cookies, data=data)
        if response.status_code == 200:
            if response.json()['code'] == 0:
                return response.json()['data']['order']['total_money']
            else:
                continue
        else:
            continue
if __name__ == '__main__':
    checkOrder()