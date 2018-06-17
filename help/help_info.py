#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
帮助信息
"""

def help_info():
    print('******************************************************************')
    print('               Information Gathering Tool 1.0                     ')
    print('******************************************************************')
    print('Description:')
    print('    Collect message')
    print()
    print('python igt.py <OPTIONS> targets')
    print('  -h   --help        Show help info ')
    print('  -t   --target      site or ip list')
    print('  -o   --output      output path')
    print('  -f   --file        open target file')
    print()
    print('  -a   --all         Perform all operations')
    print(' The following args are only valid for the ip of user input')
    print('  -i   --info        Collect ip base info')
    print('  -r   --reverseip   reverseip')
    print('  -n   --nmap        use nmap scan')
    print(' The following args are only valid for the site of user input')
    print('  -I   --address     Collect site\'s ip adress')
    print('  -w   --whois       Collect whois information')
    print('  -s   --subdomain   Collect site\'s subdomain')
    print()


if __name__ == "__main__":
    help_info()

