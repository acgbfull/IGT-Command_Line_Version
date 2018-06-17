#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controller类控制整个软件运行流程.
"""

from db.database import Database
from util.logging_show import LoggingShow
from util.parser_args import parse_args
from util.getIpDomainList import GetIpDomainList
from util.createFolderForResult import CreateFolderForResult
from util.getIpInfo import GetIpInfo
from util.getReverseIpInfo import GetReverseIpInfo
from util.getIpAddress import GetIpAddress
from util.getSubDomain import GetSubDomain
from util.whois import Whois
from util.nmapScan import nmapScan
from util.create_html import CreateHtml
import webbrowser

class Controller():
    """ initialisations that will happen once - when the program is launched.
    """
    def __init__(self):
        self.version = 'Information Gathering Tool 1.0'  # update this everytime you commit!
        self.ipDomainInputText = ""
        self.ipList = []
        self.domainList = []
        self.projectPath = ""
        self.projectName = ""
        self.projectPathText = ""
        self.checkBoxStatus = {}
        self.inputTextVerifyValue = None
        self.logging_show = None
        self.logger = None

    def start(self):
        self.initialisation()  # initialisations Values
        # check input valid or not, not return before click actionRun button
        if self.inputTextVerifyValue is False:
            return True
        try:
            self.database = Database(self.projectPath)  # sqlite数据库的初始化, 之后直接调用Database类相应的方法即可
        except Exception as error:
            self.logger.debug("-----------------------------------")
            self.logger.debug("Database Error: {0}: {1}".format(Exception, error))
        self.isSelect()

        return True

    # 初始化controller类中调用子模块(类/函数)所需要传递的变量
    # 创建存储运行结果的目录
    # 获取用户选择的功能
    def initialisation(self):
        self.checkBoxStatus = {}
        args = parse_args()

        ipDomainInputList = self.get_input_list(args)

        self.inputTextVerifyValue, self.projectName, self.ipList, self.domainList = GetIpDomainList(ipDomainInputList).start()  # 获取 输入是否合法且不为空的判断值、默认的项目名称（用于不输入项目存储路径时存储运行结果的目录名）、输入的IP列表、输入的域名列表
        if self.inputTextVerifyValue:
            self.projectPathText = "{0}".format(args.output)  # 获取用户输入的项目存储路径
            self.projectPath = CreateFolderForResult(self.projectName,
                                                     self.projectPathText).start()  # 创建存储结果数据的目录，并获取目录的路径
            self.getCheckBoxStatus(args)  # 获取用户选择的功能
            self.logging_show = LoggingShow(self.projectPath)
            self.logger = self.logging_show.get_logger()

    # 获取ui上用户勾选的功能
    def getCheckBoxStatus(self, args):
        # 获取ip function area用户选择的功能
        self.checkBoxStatus['ipInfoQuery'] = args.info
        self.checkBoxStatus['sameIpDomainQuery'] = args.reverseip
        self.checkBoxStatus['portScan'] = args.nmap

        # 获取idomain function area用户选择的功能
        self.checkBoxStatus['ipAddressQuery'] = args.address
        self.checkBoxStatus['whois'] = args.whois
        self.checkBoxStatus['subDomainQuery'] = args.subdomain
        self.checkBoxStatus['subdomainTitleGet'] = args.subdomain

        if args.all is not False:
            for key in self.checkBoxStatus.keys():
                self.checkBoxStatus[key] = True

    def get_input_list(self, args):
        if args.all is not False:
            ipDomainInputList = args.all
        if args.file is not False:
            with open(args.file, 'r') as f:
                if f:
                    file_content = f.read()
                    file_content = file_content.replace('\n', ' ')
                    ipDomainInputList = list(filter(None, file_content.split(' ')))
                else:
                    self.logger.info(u"文件内容为空")
        if args.target is not False:
            ipDomainInputList = args.target
        return ipDomainInputList

    def isSelect(self):
        # q.put(os.getpid())
        # print('child self.pid  %s.' % os.getpid())
        ipListLength = len(self.ipList)
        self.logger.info("-----------------------------------")
        self.logger.info(u"开始收集目标信息")
        for i, ip in enumerate(self.ipList):
            self.logger.info("-----------------------------------")
            self.logger.info(u"{0}\n正在处理第{1}个IP, 共{2}个".format(ip, i + 1, ipListLength))

            if self.checkBoxStatus['ipInfoQuery']:
                GetIpInfo(self.database, ip).start()
            if self.checkBoxStatus['sameIpDomainQuery']:
                GetReverseIpInfo(self.database, ip).start()
            if self.checkBoxStatus['portScan']:
                nmapScan(self.database, ip)

        domainListLength = len(self.domainList)
        for i, domain in enumerate(self.domainList):
            self.logger.info("-----------------------------------")
            self.logger.info(u"{0}\n正在处理第{1}个域名, 共{2}个".format(domain, i + 1, domainListLength))

            if self.checkBoxStatus['ipAddressQuery']:
                GetIpAddress(self.database, domain).start()
            if self.checkBoxStatus['whois']:
                Whois(self.database, domain).start()
            if self.checkBoxStatus['subDomainQuery']:
                GetSubDomain(self.database, self.checkBoxStatus['subdomainTitleGet'], domain).start()
        self.logger.info("-----------------------------------")
        self.logger.info(u"目标信息收集完毕")
        self.logger.info("-----------------------------------")

        self.logger.info(u"html文件生成中")
        CreateHtml(self.database, self.projectPath, self.ipList, self.domainList).start()
        self.logger.info(u"html文件打开中")
        webbrowser.open(u"{0}\\{1}".format(self.projectPath, "results.html"))
        self.logger.info("-----------------------------------")
        self.logger.info("执行完毕")
        self.logging_show.close()
