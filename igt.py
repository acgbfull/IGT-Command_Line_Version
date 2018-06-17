#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
主函数
Usage:
    python igt.py -a -t 120.24.248.50 acg.tv
    python igt.py -a -o "C:\Demo" -f "T:\Python Project\Information_Gathering_Tool_command\project\target.txt"
    python igt.py -i -w -t bilibili.com 120.24.248.50
    python igt.py -i -w -f "C:\test\target.txt"

"""

from controller.controller import Controller


if __name__ == "__main__":
    controller = Controller()
    controller.start()
