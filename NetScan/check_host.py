#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: check_host
# Author		: badger
# Created		: 2017/8/2
# Description	:

import os

from NetScan.util.net_check import get_ip


def check(host):
    # print(host)
    state = os.system("ping -c 1 %s" % host)
    print(state, '\n')
    pass


if __name__ == "__main__":
    ip_range = '117.87.218.1-117.87.218.255'
    for ip in get_ip(ip_range):
        check(ip)
