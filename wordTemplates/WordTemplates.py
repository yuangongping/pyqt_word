# coding: utf-8
import os
from docx import Document

class NetworkChecked(object):
    @staticmethod
    def disableNetwork():
        result = os.system(u"netsh interface set interface 以太网 disable")
        if result == 1:
            print("aaaaaa")
        else:
            print("disable")

    @classmethod
    def start_ping(cls, address):
        ip = u'ping -n 1 -w 1 ' + address
        result = os.system(ip)
        if result:
            return "网络不通, 请检查！"
        else:
            return "网络正常！"
