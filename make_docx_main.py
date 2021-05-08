# -*- coding: utf-8 -*-
import os
import time


from common.docs_deal import *

#当前脚本的绝对路径
current_path = os.path.split(os.path.realpath(__file__))[0]

if __name__ == "__main__":

    data_list = [
        {
            "sPort": 501,
            "srcIP": "192.168.50.23",
            "time": "2021-05-08T10:16:02"
        },{
            "sPort": 502,
            "srcIP": "192.168.50.23",
            "time": "2021-05-08T10:16:02"
        },{
            "sPort": 503,
            "srcIP": "192.168.50.23",
            "time": "2021-05-08T10:16:02"
        },{
            "sPort": 502,
            "srcIP": "192.168.50.23",
            "time": "2021-05-08T10:16:02"
        },{
            "sPort": 502,
            "srcIP": "192.168.50.22",
            "time": "2021-05-08T10:16:02"
        },
    ]

    time_now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    fileAllPath = os.path.join(current_path, "demo-" + time_now + ".docx" )
    make_docx(data_list, fileAllPath)