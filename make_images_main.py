# -*- coding: utf-8 -*-

import os

from common.image_deal import *

#当前脚本的绝对路径
current_path = os.path.split(os.path.realpath(__file__))[0]

if __name__ == "__main__":

    data_dict = {
        "1.1.1.1": 30,
        "1.1.1.2": 50,
        "1.1.1.3": 80,
        "1.1.1.4": 10,
    }

    fileAllPath = os.path.join(current_path)

    write_histogram_jpg(data_dict, os.path.join(current_path, "histogram.jpg"))

    write_pieChart_jpg(data_dict, os.path.join(current_path, "pieChart.jpg"))