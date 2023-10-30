#!/usr/bin/python3
""" This module is a script that computes metrics"""
import sys
try:

    ten_stats = 10
    total = 0
    for line in sys.stdin:
        i = 1
        my_list = line.split('"')
        my_dict = {}

        my_list = my_list[-1].split(" ")
        file_size = int(my_list[-1])
        status_code = int(my_list[-2])

        total += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            my_dict[status_code] = i
            ten_stats -= 1

            if ten_stats == 0:
                #my_dict = {key: my_dict[key] for key in sorted(my_dict)}
                for key in sorted(my_dict.items()):
                    print("{}: {}".format(key, my_dict[key])
            ten_stats = 10
except KeyboardInterrupt:
        if ten_stats == 0:
            #my_dict = {key: my_dict[key] for key in sorted(my_dict)}
            for key in sorted(my_dict.items()):
                 print("{}: {}".format(my_dict[key])
            ten_stats = 10
