# -*- coding: utf-8 -*-

from common.image_deal import *

if __name__ == "__main__":

    data_dict = {
        "1.1.1.1": 30,
        "1.1.1.2": 50,
        "1.1.1.3": 80,
        "1.1.1.4": 10,
    }

    write_histogram_jpg(data_dict, "./histogram.jpg")

    write_pieChart_jpg(data_dict, "./pieChart.jpg")