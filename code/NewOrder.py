# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import time

import requests
import json
import DDConf

def addNewOrder():
    cookies = {
        'DDXQSESSID': DDConf.DDXQSESSID,
    }

    headers = {
        'Host': 'maicai.api.ddxq.mobi',
        'content-type': 'application/x-www-form-urlencoded',
        'ddmc-city-number': DDConf.DDAdder.CityNumber,
        'ddmc-build-version': '2.82.0',
        'ddmc-uid': DDConf.UID,
        'ddmc-station-id': DDConf.DDAdder.StationId,
        'ddmc-channel': 'applet',
        'ddmc-os-version': '[object Undefined]',
        'ddmc-app-client-id': '4',
        'ddmc-ip': '',
        'ddmc-api-version': '9.49.2',
        'ddmc-uid': DDConf.UID,
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123f) NetType/WIFI Language/zh_CN',
        'referer': 'https://servicewechat.com/wx1e113254eda17715/422/page-frame.html',
    }
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
    package = {
        'first_selected_big_time': 0,
        'products': productList,
        'eta_trace_id': "",
        'package_id': 1,
        'reserved_time_start':DDConf.TimesList[len(DDConf.TimesList)-1]['start_timestamp'],
        'reserved_time_end':DDConf.TimesList[len(DDConf.TimesList)-1]['end_timestamp'],
        'soon_arrival':'',
        'package_type': 1,
    }
    paymentOrder = {
        'reserved_time_start':DDConf.TimesList[len(DDConf.TimesList)-1]['start_timestamp'],
        'reserved_time_end':DDConf.TimesList[len(DDConf.TimesList)-1]['end_timestamp'],
        "price": DDConf.Total_money,
        "freight_discount_money": "5.00",
        "freight_money": "5.00",
        "order_freight": "0.00",
        "parent_order_sign": DDConf.parent_order_sign,
        "product_type": 1,
        "address_id": DDConf.DDAdder.Id,
        "receipt_without_sku": 1,
        "pay_type": 6,
        "vip_money": "",
        "vip_buy_user_ticket_id": "",
        "coupons_money": "",
        "coupons_id": ""
    }
    packageOrder = {
        'payment_order':paymentOrder,
        'packages':package
    }
    packageOrderStr = str(json.dumps(packageOrder))
    data = {
        'uid':'',
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
        "package_order": packageOrderStr,
        "check_order_type": "0",
        "is_support_merge_payment": "1",
        "showData": "true",
        "showMsg": "false",
        "ab_config": "{\"key_onion\":\"C\"}"
    }
    # data = 'uid=5e075ebb9a811b874798ccba&longitude=116.317071&latitude=39.841724&station_id=5f8d0c23bac21c0001186331&city_number=0201&api_version=9.49.2&app_version=2.82.0&applet_source=&channel=applet&app_client_id=4&sharer_uid=&s_id=da911b94655cf973cfe79b77589785e9&openid=osP8I0VJqGMKA98Rar2qUwnOdeVg&h5_source=&device_token=WHJMrwNw1k%2FF0qdLNvE01AV0nGtUhf%2FMbEskbKA0IJJsIgD0pc86qnBHo6vIROLgBIKOHz%2FfQD8hjI0rJceyDXyuDTF1rRBhndCW1tldyDzmauSxIJm5Txg%3D%3D1487582755342&package_order=%7B%22payment_order%22%3A%7B%22reserved_time_start%22%3A1649458800%2C%22reserved_time_end%22%3A1649460600%2C%22price%22%3A%2224.50%22%2C%22freight_discount_money%22%3A%220.00%22%2C%22freight_money%22%3A%225.00%22%2C%22order_freight%22%3A%225.00%22%2C%22parent_order_sign%22%3A%22ef857461f7c77f9859a493d8ebcbf02f%22%2C%22product_type%22%3A1%2C%22address_id%22%3A%22624ecac9fdc0bc0001de6fd1%22%2C%22form_id%22%3A%2244d1ab3ebee04453b0c453d88902551e%22%2C%22receipt_without_sku%22%3A1%2C%22pay_type%22%3A6%2C%22vip_money%22%3A%22%22%2C%22vip_buy_user_ticket_id%22%3A%22%22%2C%22coupons_money%22%3A%22%22%2C%22coupons_id%22%3A%22%22%7D%2C%22packages%22%3A%5B%7B%22products%22%3A%5B%7B%22id%22%3A%225c1364e6716de1e77d8b61d9%22%2C%22parent_id%22%3A%22%22%2C%22count%22%3A1%2C%22cart_id%22%3A%225c1364e6716de1e77d8b61d9%22%2C%22price%22%3A%2219.50%22%2C%22product_type%22%3A0%2C%22is_booking%22%3A0%2C%22product_name%22%3A%22%E6%81%92%E9%83%BD%E7%B2%BE%E9%80%89%E5%86%B7%E5%86%BB%E8%82%A5%E7%89%9B%E5%8D%B7%20300g%22%2C%22small_image%22%3A%22https%3A%2F%2Fimg.ddimg.mobi%2Fproduct%2F2f8e629bb8e571598438426939.jpg!deliver.product.list%22%2C%22sale_batches%22%3A%7B%22batch_type%22%3A-1%7D%2C%22order_sort%22%3A1%2C%22sizes%22%3A%5B%5D%7D%5D%2C%22total_money%22%3A%2219.50%22%2C%22total_origin_money%22%3A%2219.50%22%2C%22goods_real_money%22%3A%2219.50%22%2C%22total_count%22%3A1%2C%22cart_count%22%3A1%2C%22is_presale%22%3A0%2C%22instant_rebate_money%22%3A%220.00%22%2C%22total_rebate_money%22%3A%220.00%22%2C%22used_balance_money%22%3A%220.00%22%2C%22can_used_balance_money%22%3A%220.00%22%2C%22used_point_num%22%3A0%2C%22used_point_money%22%3A%220.00%22%2C%22can_used_point_num%22%3A0%2C%22can_used_point_money%22%3A%220.00%22%2C%22is_share_station%22%3A0%2C%22only_today_products%22%3A%5B%5D%2C%22only_tomorrow_products%22%3A%5B%5D%2C%22package_type%22%3A1%2C%22package_id%22%3A1%2C%22front_package_text%22%3A%22%E5%8D%B3%E6%97%B6%E9%85%8D%E9%80%81%22%2C%22front_package_type%22%3A0%2C%22front_package_stock_color%22%3A%22%232FB157%22%2C%22front_package_bg_color%22%3A%22%23fbfefc%22%2C%22eta_trace_id%22%3A%2216494187769211970306781%22%2C%22reserved_time_start%22%3A1649458800%2C%22reserved_time_end%22%3A1649460600%2C%22soon_arrival%22%3A%22%22%2C%22first_selected_big_time%22%3A0%7D%5D%7D&showMsg=false&showData=true&ab_config=%7B%22key_onion%22%3A%22C%22%7D&nars=d70660bc0b63af013578f42b8b19ce7d&sesi=V3V3sRZ39acce8ec3d6d141f18a318a0c365910'
    for num in range(1, 100):
        response = requests.post('https://maicai.api.ddxq.mobi/order/addNewOrder', headers=headers, cookies=cookies, data=data)
        print('下单接口：'+str(response.json()))
        if response.status_code == 200:
            if response.json()['code']==0:
                return 200
            else:
                # time.sleep(0.3)
                continue
