#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
nmapScan函数的功能:
    调用nmap对指定ip进行扫描.
"""

import os
from config import config
import logging


def nmapScan(database, ip, nmapParameter = config.nmap_cmd_line):
    try:
        cmd = "{0} {1} {2}".format("nmap.exe", nmapParameter, ip)
        logging.getLogger("real_time_info").info("{0}".format(cmd))
        result = os.popen(cmd).read()
        database.addNmapResult(ip, cmd, result)
        logging.getLogger("real_time_info").info("成功获取端口信息")
    except Exception as error:
        logging.getLogger("real_time_info").info("获取端口信息失败, Error：{0}: {1}".format(Exception, error))
