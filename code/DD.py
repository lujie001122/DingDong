# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import Address
import DDConf
import Cart
import ReserveTime
import Order
import NewOrder
import requests
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
scheduler = BlockingScheduler()


def print_hi(name="haha"):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def Bark():
    for num in range(1, 5):
        Bark = DDConf.Bark
        requests.get('https://api.day.app/'+Bark+'/起床买菜')

@scheduler.scheduled_job('cron',hour="*",minute="0-59", second='*/1',max_instances=10)
def task():
    try:
        print("开始抢菜")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        addres = Address.getAddress();
        DDConf.DDAdder = addres[0]
        print("抢菜地址：" + DDConf.DDAdder.Name)

        products, parent_order_sign = Cart.checkCart()
        DDConf.Products = products
        if len(products) == 0:
            print("购物车空了")
        if len(products) > 0:
            print("抢菜的商品：")
            print(products)
            DDConf.parent_order_sign = parent_order_sign
            times = ReserveTime.GetMultiReserveTime()
            DDConf.TimesList = times
            print("抢菜运力时间段")
            print(times)
            if len(times) == 0:
                print("该时段暂无运力")
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            else:
                Total_money = Order.checkOrder()
                DDConf.Total_money = Total_money
                print("预计花费：", Total_money)

                code = NewOrder.addNewOrder()
                if code == 200:
                    print("抢到菜啦，快起来支付！！！")
                    Bark()
                    sys.exit(0)
    except Exception as ex:
        print(ex)
        print("网络错误，勿惊")
def run():
    try:
        scheduler.start()
    except Exception as ex:
        print(ex)
        print('定时任务错误')
        print('定时任务错误')
        print('定时任务错误')
        scheduler.shutdown()
if __name__ == '__main__':
    task()
    # schedule.every(10).seconds.do(task)
    # while True:
    #     schedule.run_pending()
