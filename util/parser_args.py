#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
命令行参数定义
"""

import argparse
from argparse import RawTextHelpFormatter


def parse_args():
    description = "Description:\n    Collect message"
    usage = "python igt.py -a -t ip/site(s)\n       " \
            "python igt.py -i -r -s -t ip/site(s)\n       " \
            "python igt.py -a -o outputPath -f filePath\n"
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=description, usage=usage)

    #parser.add_argument('target', nargs='+', help="ip or site list", default=False)
    parser.add_argument('-a', '--all', action='store_true', help="Perform all operations", required=False, default=False)
    parser.add_argument('-i', '--info', help="Collect ip base info", action='store_true', required=False, default=False)
    parser.add_argument('-r', '--reverseip', help="reverseip", action='store_true', required=False, default=False)
    parser.add_argument('-n', '--nmap', help="use nmap scan", action='store_true', required=False, default=False)
    parser.add_argument('-I', '--address', help="Collect site\'s ip adress", action='store_true', required=False, default=False)
    parser.add_argument('-w', '--whois', help="Collect whois information", action='store_true', required=False, default=False)
    parser.add_argument('-s', '--subdomain', help="Collect site\'s subdomain", action='store_true', required=False, default=False)

    parser.add_argument('-o', '--output', help="output path", required=False, default=False)
    parser.add_argument('-f', '--file', help="open target file", required=False, default=False)
    parser.add_argument('-t', '--target', nargs='+', help="ip or site list", required=False, default=False)
    #parser.add_argument('-np', '--nmapParameter', help="use nmap scan by custom parameters", required=False, default=None)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    print("args = ", args)
    print(type(args.all), " args.all = ", args.all)
    print(type(args.target), " args.target = ", args.target)
    if args.all is True:
        print("args.all is True")
    if args.all is not False:
        print("args.all is not False")

