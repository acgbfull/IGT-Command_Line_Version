# IGT(command-line version)

## Description

**IGT**是一款具有收集IP地理位置、同IP网站、端口信息、IP地址、WHOIS、子域名信息的工具。
（IGT is a tool for collecting IP Location, reverse IP info, port info, IP address, WHOIS, subdomains info.）


## Operating environment

> python 3+
>
> window 7
>
> nmap （nmap添加到环境变量中）


## Configuration Guide
配置文件：config/config.py <br>
可设置http请求超时时间和nmap扫描时的默认参数. <br>
生成的results.html、保有数据的数据库文件和log文件默认保存于程序根目录下的project目录. <br>


## Installation guide

>git clone https://github.com/acgbfull/IGT-Command_Line_Version.git


## help
        ******************************************************************
                     Information Gathering Tool 1.0                     
         ******************************************************************
         Description:
             Collect message
         
         usage:python igt.py -a -t ip/site(s)
                    python igt.py -i -r -s -t ip/site(s)
                    python igt.py -a -o outputPath -f filePath

         -h   --help        Show help info 
         -t   --target      site or ip list
         -o   --output      output path
         -f   --file        open target file
         
         -a   --all         Perform all operations
          The following args are only valid for the ip of user input
         -i   --info        Collect ip base info
         -r   --reverseip   reverseip
         -n   --nmap        use nmap scan
         The following args are only valid for the site of user input
         -I   --address     Collect site\s ip adress
         -w   --whois       Collect whois information
         -s   --subdomain   Collect site\s subdomain


## Usage

> python igt.py -a -t 120.24.248.50 acg.tv
>
> python igt.py -a -o "C:\Demo" -f "E:\project\target.txt"
>
> python igt.py -i -w -t bilibili.com 120.24.248.50
>
> python igt.py -i -w -f "C:\test\target.txt"


## Demo

python igt.py -a -t bilibili.com 120.24.248.50

**程序运行中**

![run截图](https://github.com/acgbfull/IGT-Command_Line_Version/raw/master/images/run.png "UI截图")

**程序运行生成的results.html**

![result截图](https://github.com/acgbfull/IGT-Command_Line_Version/raw/master/images/result.png "UI截图")


## CHANGE LOG

>2018/6/17  version:1.0.0

