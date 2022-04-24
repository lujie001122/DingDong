# -*- coding:utf-8 -*-
# __author__ = 'lujie'
import DD
import DDConf


def gui():
    cookie = input("请输入cookie：")
    DDConf.DDXQSESSID = cookie
    print("你输入的cookie是: ", DDConf.DDXQSESSID)

    uid = input("请输入uid：")
    DDConf.UID = uid
    print("你输入的uid是: ", DDConf.UID)

    Bark = input("请输入Bark：")
    DDConf.Bark = Bark
    print("你输入的Bark是: ", DDConf.Bark)

    DD.run()

if __name__ == '__main__':
    gui()