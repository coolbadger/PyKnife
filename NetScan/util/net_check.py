#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: check_host
# Author		: badger
# Created		: 2017/8/4
# Description	: 

from socket import *

TIME_OUT = 0.01


def check_host(host):
    state = os.system("ping -c 1 " + host)
    if state == 0:
        return True
    else:
        return False


def check_port(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(TIME_OUT)
        s.connect((host, port))
        print(host + '\t[+] %d open' % port)
        s.close()
        return True
    except:
        print(host + '\t[-] %d close' % port)
        return False


def get_ip(host):
    return gethostbyname(host)


def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]


def num2ip(num):
    return '%s.%s.%s.%s' % ((num & 0xff000000) >> 24,
                            (num & 0x00ff0000) >> 16,
                            (num & 0x0000ff00) >> 8,
                            num & 0x000000ff)


def get_ip(ip):
    start, end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start, end + 1) if num & 0xff]


# print(get_ip('192.168.31.1-192.168.32.1'))
